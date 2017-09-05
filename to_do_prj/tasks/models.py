from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=254, blank=False)
    description = models.TextField(blank=False)
    status = models.CharField(max_length=254)

    def __str__(self):
        return self.name
