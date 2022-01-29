from django.db import models
from django.utils.text import slugify


class Products(models.Model):

    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    code = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
