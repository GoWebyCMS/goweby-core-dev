from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse

from category.models import Category
# custom model managers

# a custom published manager
# custom model managers
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super (PublishedManager, self).get_queryset().filter(status='published')

# Create your models here.


class ProjectCategory(Category):

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Skill(Category):

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"


class Project(models.Model):
    STATUS_CHOICES = (
            ('draft', 'Draft'),
            ('completed', 'Completed'),
        )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    url = models.URLField(blank=True, null=True)
    short_description = models.CharField(max_length=350)
    description = RichTextField()
    job = models.CharField(max_length=200, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    client = models.CharField(max_length=200, blank=True, null=True)
    categories = models.ForeignKey('ProjectCategory', blank=True, null=True, related_name="project_categories")
    skills = models.ManyToManyField('Skill', related_name="project_skills")
    featured_image = models.ImageField(upload_to='portfolio', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    def get_absolute_url(self):
        return reverse('portfolio_detail',args=[self.slug])

    class Meta:
        ordering = [ 'end_date', ]

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()
