from django.db import models

# one to many relation between models
# typically reference ownership

class User(models.Model):
    name = models.CharField(max_length=55)
    age = models.IntegerField()
    desc = models.TextField(default = "old")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class vGame(models.Model):
    title = models.CharField(max_length=55)
    is_multiplayer = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    player = models.ForeignKey(User, related_name="vGames", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)