from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    state = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ninja(models.Model):
    fname = models.CharField(max_length=55)
    lname = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    dojos = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)