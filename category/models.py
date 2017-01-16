from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()

    class Meta:
        abstract = True

    def __str__(slef):
        return self.name
