# courses/admin.py
from django.contrib import admin
from .models import Course, CourseCategory

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'current_price', 'is_featured', 'level')
    list_filter = ('category', 'is_featured', 'level')
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}