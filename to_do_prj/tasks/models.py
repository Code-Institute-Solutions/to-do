from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    status = models.CharField(max_length=254)
    
    def __str__(self):
        return self.name
    
    objects = models.Manager()