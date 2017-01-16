from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.core.urlresolvers import reverse

from category.models import Category

# create model manager for Posts to include custom filter
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

# Create your models here.

class Category(Category):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Tag(Category):

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Post(models.Model):
    STATUS_CHOICES = (
            ('draft', 'Draft'),
            ('published', 'Published'),
        )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', blank=True, null=True)
    category = models.ForeignKey(Category, related_name='post_category')
    tags = models.ManyToManyField(Tag, related_name='post_tag')
    featured = models.BooleanField(default=False)
    body = RichTextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    featured_image = models.ImageField(upload_to='post_images', blank=True, null=True)

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    def get_absolute_url(self):
        return reverse('post_detail',
                       args=[self.slug])

    class Meta:
        ordering = ('-featured','publish',)

    def __str__(self):
        return self.title
