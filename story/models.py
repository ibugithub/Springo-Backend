from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Story(models.Model):
    name = models.CharField(max_length=100)
    story = models.TextField()
    def __str__(self):
        return self.name
