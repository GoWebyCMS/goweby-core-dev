from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        abstract = True
        ordering = ('name',)


    def __str__(self):
        return self.name
