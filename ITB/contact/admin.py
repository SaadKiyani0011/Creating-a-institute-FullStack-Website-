from django.contrib import admin
from contact.models import Contact, SiteContactInfo
from django.utils.html import format_html
from django.urls import reverse

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # Configuration for the Contact model admin interface

    # Fields to display in the list view
    list_display = (
        'truncated_name',
        'email_link',
        'short_subject',
        'formatted_date',
        'status_badge',
        'actions'
    )

    # Fields to filter by in the right sidebar
    list_filter = (
        'is_resolved',
        'submitted_at'
    )

    # Fields to search by
    search_fields = (
        'name',
        'email',
        'subject',
        'message'
    )

    # Fields that can be edited directly in the list view
    list_editable = (
        'is_resolved',
    )

    # Date-based navigation at the top
    date_hierarchy = 'submitted_at'

    # Fields grouped in the edit view
    fieldsets = (
        ('Contact Information', {
            'fields': (
                'name',
                'email',
                'subject'
            )
        }),
        ('Message Content', {
            'fields': (
                'message',
            ),
            'classes': ('wide',)
        }),
        ('Status', {
            'fields': (
                'is_resolved',
            ),
            'classes': ('collapse',)
        })
    )

    # Custom methods for list display
    def truncated_name(self, obj):
        return obj.name[:20] + '...' if len(obj.name) > 20 else obj.name
    truncated_name.short_description = 'Name'
    truncated_name.admin_order_field = 'name'

    def email_link(self, obj):
        return format_html('<a href="mailto:{}">{}</a>', obj.email, obj.email)
    email_link.short_description = 'Email'
    email_link.admin_order_field = 'email'

    def short_subject(self, obj):
        return obj.subject[:30] + '...' if obj.subject and len(obj.subject) > 30 else obj.subject or 'No Subject'
    short_subject.short_description = 'Subject'
    short_subject.admin_order_field = 'subject'

    def formatted_date(self, obj):
        return obj.submitted_at.strftime("%b %d, %Y %H:%M")
    formatted_date.short_description = 'Submitted'
    formatted_date.admin_order_field = 'submitted_at'

    def status_badge(self, obj):
        if obj.is_resolved:
            return format_html(
                '<span style="color: green; font-weight: bold;">✓ Resolved</span>'
            )
        return format_html(
            '<span style="color: red; font-weight: bold;">✗ Pending</span>'
        )
    status_badge.short_description = 'Status'
    status_badge.admin_order_field = 'is_resolved'

    def actions(self, obj):
        view_url = reverse('admin:contact_contact_change', args=[obj.id])
        return format_html(
            '<a class="button" href="{}">View/Reply</a>',
            view_url
        )
    actions.short_description = 'Actions'

    # Add custom admin actions
    actions = ['mark_as_resolved', 'mark_as_pending', 'export_contacts']

    def mark_as_resolved(self, request, queryset):
        queryset.update(is_resolved=True)
        self.message_user(request, f"Marked {queryset.count()} contacts as resolved")
    mark_as_resolved.short_description = "Mark selected as resolved"

    def mark_as_pending(self, request, queryset):
        queryset.update(is_resolved=False)
        self.message_user(request, f"Marked {queryset.count()} contacts as pending")
    mark_as_pending.short_description = "Mark selected as pending"

    def export_contacts(self, request, queryset):
        import csv
        from django.http import HttpResponse
        from io import StringIO

        output = StringIO()
        writer = csv.writer(output)
        
        # Write headers
        writer.writerow([
            'ID', 'Name', 'Email', 'Subject', 
            'Message Excerpt', 'Submitted At', 'Status'
        ])
        
        # Write data
        for contact in queryset:
            writer.writerow([
                contact.id,
                contact.name,
                contact.email,
                contact.subject or 'No Subject',
                contact.message[:100] + '...' if len(contact.message) > 100 else contact.message,
                contact.submitted_at.strftime("%Y-%m-%d %H:%M"),
                'Resolved' if contact.is_resolved else 'Pending'
            ])
        
        output.seek(0)
        response = HttpResponse(output, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=contact_submissions.csv'
        return response
    export_contacts.short_description = "Export selected contacts"

@admin.register(SiteContactInfo)
class SiteContactInfoAdmin(admin.ModelAdmin):
    # Configuration for the SiteContactInfo model (singleton pattern)

    def has_add_permission(self, request):
        # Only allow one instance to exist
        return not SiteContactInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of the only instance
        return False

    fieldsets = (
        ('Basic Information', {
            'fields': (
                'address',
                'phone',
                'email'
            )
        }),
        ('Social Media Links', {
            'fields': (
                'facebook_url',
                'twitter_url',
                'instagram_url',
                'linkedin_url'
            ),
            'classes': ('wide',)
        })
    )

    def social_links(self, obj):
        links = []
        if obj.facebook_url:
            links.append(f'<a href="{obj.facebook_url}" target="_blank">Facebook</a>')
        if obj.twitter_url:
            links.append(f'<a href="{obj.twitter_url}" target="_blank">Twitter</a>')
        if obj.instagram_url:
            links.append(f'<a href="{obj.instagram_url}" target="_blank">Instagram</a>')
        if obj.linkedin_url:
            links.append(f'<a href="{obj.linkedin_url}" target="_blank">LinkedIn</a>')
        return format_html(' | '.join(links)) if links else 'No social links'
    social_links.short_description = 'Social Media'

    list_display = ('address', 'phone', 'email', 'social_links')