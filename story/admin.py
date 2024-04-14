from django.contrib import admin
from .models import Story

registerModel = [ Story, ]
admin.site.register(registerModel)