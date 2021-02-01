from django.db import models
import re

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData ['fname']) < 2:
            errors['fname'] = 'First name must be 2 chars or more.'
        if len(postData ['lname']) < 2:
            errors['lname'] = 'Last name must be 2 chars or more.'
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
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(models.Model):
    message = models.CharField(max_length=255)
    userPost = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    userComment = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="post", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


