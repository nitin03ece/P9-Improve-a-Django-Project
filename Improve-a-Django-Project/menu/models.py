from django.db import models
from django.utils import timezone


class Menu(models.Model):
    items = models.ManyToManyField('Item')
    season = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.season


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    chef = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    standard = models.BooleanField(default=False)
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.name

    def item_name(self):
        name = self.name.split()
        name = name[0:5]
        name = " ".join(name)
        return name


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
