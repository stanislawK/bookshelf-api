from django.db import models


class AuthorModel(models.Model):
    """Author object"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CategoryModel(models.Model):
    """Category object"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BookModel(models.Model):
    """Book object"""
    title = models.CharField(max_length=300)
    description = models.TextField()
    authors = models.ManyToManyField(AuthorModel)
    categories = models.ManyToManyField(CategoryModel)

    def __str__(self):
        return self.title
