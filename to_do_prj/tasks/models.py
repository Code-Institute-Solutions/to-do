from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=254, blank=False)
    description = models.TextField(blank=False)
    done=models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.name
