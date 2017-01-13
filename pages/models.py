from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.

class Page(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
    menu_title = models.CharField(max_length=200)
    page_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique_for_date='publish')
    body = RichTextField()
    show_in_menu = models.BooleanField(default=False)
    publish = models.DateTimeField( auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    image = models.ImageField(upload_to='page', blank=True, null=True)


    def get_absolute_url(self):
        return reverse('page_detail',
                       args=[self.slug])

    class Meta:
        ordering = ('page_title',)


    def __str__(self):
        return self.page_title
