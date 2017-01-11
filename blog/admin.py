from django.contrib import admin
from .models import Post, Category, Tag

# Customize the way models are displayed


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}



class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'slug', 'author', 'publish', 'status', 'featured')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

# Register your models here.

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
