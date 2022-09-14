from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=80)
    website = models.URLField(max_length=100)