from django.test import TestCase
from django.utils import timezone
from blog.models import Post

class PostModelTest(TestCase):
    def test_creating_a_new_post_and_saving_it_to_the_database(self):
        # start by creating a new Post object
        post = Post()
        post.title = "Test Post Title"
        post.pub_date = timezone.now()

        # check we can save it to the database
        post.save()

        # now check we can find it in the database again
        all_posts_in_database = Post.objects.all()
        self.assertEquals(len(all_posts_in_database), 1)
        only_post_in_database = all_posts_in_database[0]
        self.assertEquals(only_post_in_database, post)

        # and check that it's saved its two attributes: title and pub_date
        self.assertEquals(only_post_in_database.title, "Test Post Title")
        self.assertEquals(only_post_in_database.publish, post.publish)


    def test_root_url_shows_all_posts(self):
        # setup some posts
        post1 = Post(title='Test Post One', publish=timezone.now())
        post1.save()
        post2 = Post(title='Test Post Two', publish=timezone.now())
        post2.save()

        response = self.client.get('/')

        # check we've used the right template
        self.assertTemplateUsed(response, 'blog/post/list.html')
