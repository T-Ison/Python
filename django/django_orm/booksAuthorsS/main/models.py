from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=55)
    desc = models.TextField(default = "No Description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    fname = models.CharField(max_length=55)
    lname = models.CharField(max_length=55)
    notes = models.TextField(default = "No Description")
    books = models.ManyToManyField(Book, related_name="authors")
    updated_at = models.DateTimeField(auto_now=True)