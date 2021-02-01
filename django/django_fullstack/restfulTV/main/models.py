from django.db import models

class ShowManager(models.Manager):
    def validator(self, postData):
        errs = {}
        if len(postData['title']) < 4:
            errs['title'] = 'Title must be longer than 3 characters.'
        return errs

class tvShow(models.Model):
    title = models.CharField(max_length=55)
    reDate = models.DateField()
    desc = models.CharField(max_length=255, default="No Description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

class Network(models.Model):
    name = models.CharField(max_length=25)
    shows = models.ManyToManyField(tvShow, related_name= 'networks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
