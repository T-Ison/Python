from django.db import models
import re

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData ['name']) < 2:
            errors['name'] = 'Name must be 2 chars or more.'
        if len(postData ['alias']) < 2:
            errors['alias'] = 'Alias must be 2 chars or more.'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData ['password']) < 8:
            errors['password'] = "Passwords must be 8 chars or more."
        if postData ['password'] != postData['confirm_password']:
            errors['confirm'] = "Passwords don't match."
        return errors

    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData ['password']) < 8:
            errors['password'] = "Passwords must be 8 chars or more."
        return errors



class User(models.Model):
    name = models.CharField(max_length=25)
    alias = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=25)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    submitter = models.ForeignKey(User, related_name='submitted_books', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    content = models.CharField(max_length=25)
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, related_name='reviews_submitted', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)