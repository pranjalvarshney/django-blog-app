from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=3000)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField()