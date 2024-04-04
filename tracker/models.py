from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    COMPANY_TYPES = (
        ('tech', 'Technology'),
        ('finance', 'Finance'),
        ('retail', 'Retail'),
        ('healthcare', 'Healthcare'),
        ('manufacturing', 'Manufacturing'),
        ('education', 'Education'),
        ('consulting', 'Consulting')
    )
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=COMPANY_TYPES)
    def __str__(self):
        return self.name

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    
class Device(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

class Transaction(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checked_out = models.DateTimeField()
    checked_in = models.DateTimeField()
    condition_on_checkout = models.CharField(max_length=100)
    condition_on_checkin = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.employee} - {self.device} - Checked out: {self.checked_out}"

