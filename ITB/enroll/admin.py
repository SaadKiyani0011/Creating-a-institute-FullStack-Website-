from django.contrib import admin
from .models import Enrollment, Program
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe

class EnrollmentAdmin(admin.ModelAdmin):
    # Display fields in list view
    list_display = (
        'application_id',
        'applicant_name',
        'program_display',
        'enrollment_type',
        'application_date',
        'approval_status',
        'preview_application',
        'actions'
    )
    
    # Filter options
    list_filter = (
        'enrollment_type',
        'highest_qualification',
        'is_approved',
        'application_date'
    )
    
    # Search functionality
    search_fields = (
        'full_name',
        'email',
        'phone',
        'program'
    )
    
    # Make these fields read-only when editing
    readonly_fields = (
        'application_date',
        'documents_preview'
    )
    
    # Fields to display in edit view
    fieldsets = (
        ('Personal Information', {
            'fields': (
                'full_name',
                'date_of_birth',
                'email',
                'phone'
            )
        }),
        ('Academic Background', {
            'fields': (
                'last_school',
                'highest_qualification',
                'year_completed'
            )
        }),
        ('Program Details', {
            'fields': (
                'program',
                'enrollment_type'
            )
        }),
        ('Documents', {
            'fields': (
                'documents_preview',
                'transcript',
                'id_proof'
            )
        }),
        ('Administration', {
            'fields': (
                'is_approved',
                'application_date'
            ),
            'classes': ('collapse',)
        })
    )
    
    # Custom methods for list display
    def applicant_name(self, obj):
        return obj.full_name
    applicant_name.short_description = 'Applicant'
    applicant_name.admin_order_field = 'full_name'
    
    def program_display(self, obj):
        return obj.program
    program_display.short_description = 'Program'
    
    def approval_status(self, obj):
        if obj.is_approved:
            return format_html('<span style="color: green;">✓ Approved</span>')
        return format_html('<span style="color: red;">× Pending</span>')
    approval_status.short_description = 'Status'
    
    def application_id(self, obj):
        return f"APP-{obj.id:04d}"
    application_id.short_description = 'ID'
    
    def documents_preview(self, obj):
        links = []
        if obj.transcript:
            links.append(f'<a href="{obj.transcript.url}" target="_blank">View Transcript</a>')
        if obj.id_proof:
            links.append(f'<a href="{obj.id_proof.url}" target="_blank">View ID Proof</a>')
        return mark_safe(' | '.join(links)) if links else 'No documents'
    documents_preview.short_description = 'Documents'
    
    def actions(self, obj):
        return format_html(
            '<a class="button" href="{}">View</a>&nbsp;'
            '<a class="button" href="{}">Edit</a>',
            reverse('admin:enroll_enrollment_change', args=[obj.id]),
            reverse('admin:enroll_enrollment_change', args=[obj.id])
        )
    actions.short_description = 'Actions'
    actions.allow_tags = True

    def preview_application(self, obj):
        url = reverse('enrollment_preview', args=[obj.id])
        return format_html('<a class="button" href="{}" target="_blank">Preview</a>', url)
    preview_application.short_description = 'Preview'

    def approve_applications(self, request, queryset):
        queryset.update(is_approved=True)
    approve_applications.short_description = "Approve selected applications"

    def save_model(self, request, obj, form, change):
        if 'transcript' in form.changed_data or 'id_proof' in form.changed_data:
            # Add your document handling logic here
            pass
        super().save_model(request, obj, form, change)

    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="enrollments.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'ID', 'Name', 'Email', 'Phone', 'Program', 
            'Enrollment Type', 'Status', 'Application Date'
        ])

        for obj in queryset:
            writer.writerow([
                f"APP-{obj.id:04d}",
                obj.full_name,
                obj.email,
                obj.phone,
                obj.program,
                obj.get_enrollment_type_display(),
                "Approved" if obj.is_approved else "Pending",
                obj.application_date.strftime("%Y-%m-%d")
            ])

        return response
    export_as_csv.short_description = "Export Selected"

    # Register actions
    actions = ['export_as_csv', 'approve_applications']

admin.site.register(Enrollment, EnrollmentAdmin)


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'active_status', 'created_enrollments')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    actions = ['activate_programs', 'deactivate_programs']
    
    def active_status(self, obj):
        return "Active" if obj.is_active else "Inactive"
    active_status.short_description = 'Status'
    
    def created_enrollments(self, obj):
        count = obj.enrollment_set.count()
        url = (
            reverse("admin:enroll_enrollment_changelist") 
            + f"?program__id__exact={obj.id}"
        )
        return format_html('<a href="{}">{} enrollments</a>', url, count)
    created_enrollments.short_description = 'Enrollments'
    
    def activate_programs(self, request, queryset):
        queryset.update(is_active=True)
    activate_programs.short_description = "Activate selected programs"
    
    def deactivate_programs(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_programs.short_description = "Deactivate selected programs"
