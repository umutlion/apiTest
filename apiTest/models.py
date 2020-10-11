from django.db import models


# Create your models here.
class AbstractModel(models.Model):
    date_published = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        abstract = True


class Category(AbstractModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(AbstractModel):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    category = models.ForeignKey('apiTest.Category', on_delete=models.DO_NOTHING, null=True, blank=True)

    def get_category_name(self):
        if self.category:
            return self.category.name
        else:
            return None

    def __str__(self):
        return self.title
