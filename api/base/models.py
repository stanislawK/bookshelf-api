from django.db import models


class AuthorModel(models.Model):
    """Author object"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CategoryModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
