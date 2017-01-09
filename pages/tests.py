from django.test import TestCase
from django.utils import timezone
from pages.models import Page

from django.test import TestCase
from django.utils import timezone
from blog.models import Post

class PageModelTest(TestCase):
    def test_creating_a_new_page_and_saving_it_to_the_database(self):
        # start by creating a new Page object
        page = Page()
        page.title = "Test Page Title"

        # check we can save it to the database
        page.save()

        # now check we can find it in the database again
        all_pages_in_database = Page.objects.all()
        self.assertEquals(len(all_pages_in_database), 1)
        only_page_in_database = all_pages_in_database[0]
        self.assertEquals(only_page_in_database, page)

        # and check that it's saved its two attributes: title and pub_date
        self.assertEquals(only_page_in_database.title, "Test Page Title")
        self.assertEquals(only_page_in_database.publish, page.publish)


    def test_root_url_shows_all_pages(self):

        response = self.client.get('/pages/1')

        # check we've used the right template
        self.assertTemplateUsed(response, 'page/page_detail.html')
