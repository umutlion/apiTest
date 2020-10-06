from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=6000)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
