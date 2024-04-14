from rest_framework import serializers
from .models import Story
from django.contrib.auth.models import User

class StorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Story
    fields = ['id', 'name', 'story']
