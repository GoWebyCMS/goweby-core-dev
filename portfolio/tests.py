from django.test import TestCase
from django.core.urlresolvers import resolve
from portfolio.views import home_page
from django.http import HttpRequest

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/portfolio')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Portfolio App</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
