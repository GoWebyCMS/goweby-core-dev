from django.test import TestCase
from django.core.urlresolvers import resolve
from portfolio.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

from portfolio.models import Project

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/portfolio')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        # test implementation instead of testing constants
        self.assertEqual(response.content.decode(), response)


class ProjectModelTest(TestCase):
    def test_saving_retrieving_projects(self):
        first_project = Project()
        first_project.name = "The first ever test project"
        first_project.save()

        second_project = Project()
        second_project.name = "The second test project"
        second_project.save()

        saved_projects = Project.objects.all()
        self.assertEqual(saved_projects.count(),2)

        first_saved_project = saved_projects[0]
        second_saved_project = saved_projects[1]
        self.assertEqual(first_saved_project.name,'The first ever test project')
        self.assertEqual(second_saved_project.name, 'The second test project')
