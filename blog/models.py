from django.db import models

# Create your models here.

class words(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField(auto_now=True)
    popular = models.BooleanField(default=False)
    category = models.CharField(max_length=20,default='Uncategorized')
