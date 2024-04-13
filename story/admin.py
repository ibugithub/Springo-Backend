from django.contrib import admin
from .models import Company, Employee, Story, Transaction

registerModel = [Company, Employee, Story, Transaction]
admin.site.register(registerModel)