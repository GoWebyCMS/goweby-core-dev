from django.test import TestCase
from django.core.urlresolvers import resolve
from portfolio.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

from portfolio.models import Project
from portfolio.views import portfolio_list, home_page, portfolio_details

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/portfolio_home/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        # test implementation instead of testing constants
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)


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

class PortfolioListPageTest(TestCase):

    def test_portfolio_list_url_resolves_portfolio_list_view(self):
        url_found = resolve('/portfolio_home/portfolio_list/')
        self.assertEqual(url_found.func, portfolio_list)

    def test_portfolio_list_returns_correct_html(self):
        request = HttpRequest()
        response = portfolio_list(request)
        expected_html = render_to_string('portfolio/portfolio_list.html')
        self.assertEqual(response.content.decode(), expected_html)

class PortfolioDetailsPageTest(TestCase):

    def test_portfolio_details_url_resolves_portfolio_detail_view(self):
        det_found = resolve('/portfolio_home/(?P<pk>[0-9]+)/')
        self.assertEqual(det_found.func, portfolio_list)

    def test_portfolio_details_returns_correct_html(self):
        request = HttpRequest()
        response = portfolio_details(request, 1)
        expected_html = render_to_string('portfolio/portfolio_details.html')
        self.assertEqual(response.content.decode(), expected_html)
