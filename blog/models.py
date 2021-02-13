from django.db import models

# Create your models here.

class DailyFeed(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    thoughts = models.CharField(max_length=300)

class NewPost(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images')
    date = models.DateTimeField(auto_now_add=True)


