from django.contrib import admin
from services_a.models import Service, ServiceFeature

class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'service_type', 'is_featured', 'display_order')
    list_filter = ('service_type', 'is_featured')
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ServiceFeatureInline]
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'service_type', 'icon_class')
        }),
        ('Content', {
            'fields': ('short_description', 'full_description')
        }),
        ('Display', {
            'fields': ('is_featured', 'badge_text', 'display_order', 'cta_text')
        }),
    )