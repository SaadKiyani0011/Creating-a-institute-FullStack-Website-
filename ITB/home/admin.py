from django.contrib import admin
from home.models import Course, MissionVision, TeamMember

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_featured')
    list_editable = ('order', 'is_featured')

@admin.register(MissionVision)
class MissionVisionAdmin(admin.ModelAdmin):
    pass

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'is_ceo')
    list_editable = ('is_ceo',)