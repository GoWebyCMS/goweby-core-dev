from django.test import TestCase
from django.core.urlresolvers import resolve
from portfolio.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/portfolio')
        self.assertEqual(found.func, home_page)
