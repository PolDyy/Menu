from django.db import models


# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=25, unique=True)
    slug = models.SlugField(max_length=25)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

