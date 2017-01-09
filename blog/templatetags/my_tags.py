from django import template
from pages.models import Page
register = template.Library()

@register.inclusion_tag('page/pages_menu.html')
def show_pages_menu(pages_menu):
    pages_menu = Page.objects.filter(show_in_menu=True)
    return { 'pages_menu' : pages_menu }
