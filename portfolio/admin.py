from django.contrib import admin

from .models import Project, Category
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('name', 'short_description', 'category', 'status', )
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
