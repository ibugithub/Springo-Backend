from django.contrib import admin
from .models import Company, Employee, Device, Transaction

registerModel = [Company, Employee, Device, Transaction]
admin.site.register(registerModel)