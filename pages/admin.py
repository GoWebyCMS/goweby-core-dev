from django.contrib import admin

from .models import Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    model = Page
    list_display = ('page_title', 'slug', 'status', 'show_in_menu',)
    prepopulated_fields = {'slug': ('page_title',)}

# Register your models here.

admin.site.register(Page, PageAdmin)
