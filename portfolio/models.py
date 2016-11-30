from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# custom model managers

# a custom published manager
# custom model managers
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super (PublishedManager, self).get_queryset().filter(status='published')

# Create your models here.

class Project(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    short_description = models.TextField(blank=True, null=True)
    description = RichTextField()
    date = models.DateField(blank=True, null=True)
    client = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey('Category', blank=True, null=True, related_name="projects")
    image = models.ImageField(upload_to='portfolio', blank=True, null=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')


    class Meta:
        ordering = [ 'date', ]

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
