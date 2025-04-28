from django.db import models
from django.urls import reverse


# Category model
class Category(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


# Product model
class Product(models.Model):
    image = models.ImageField(upload_to='products/', blank=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text')
    price = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("mainapp:product", kwargs={
            'slug': self.slug
        })
