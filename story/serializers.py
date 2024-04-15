from rest_framework import serializers
from .models import Story
from django.contrib.auth.models import User

class StorySerializer(serializers.ModelSerializer):
  author = serializers.HiddenField(default=serializers.CurrentUserDefault())
  class Meta:
    model = Story
    fields = ['id', 'name', 'story', 'author']
