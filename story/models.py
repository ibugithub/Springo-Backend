from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Story(models.Model):
    name = models.CharField(max_length=100)
    story = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
