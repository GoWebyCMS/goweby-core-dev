from .models import Page


def show_pages_menu(context):
    pages_menu = Page.objects.filter(show_in_menu=True)
    foo = 3
    return { 'pages_menu' : pages_menu,  'foo' : foo }
