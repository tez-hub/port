from django.db import models

# Create your models here.

class Projects(models.Model):
    img = models.ImageField()
    url = models.CharField(max_length=200)