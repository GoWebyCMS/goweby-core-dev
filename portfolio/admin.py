from django.contrib import admin

from .models import Project, ProjectCategory, Skill
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    model = ProjectCategory
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class SkillAdmin(admin.ModelAdmin):
    model = Skill
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('name', 'short_description', 'categories', 'status', )
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory, CategoryAdmin)
admin.site.register(Skill, SkillAdmin)
