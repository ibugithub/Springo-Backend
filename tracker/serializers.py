from rest_framework import serializers
from .models import Company, Employee, Device, Transaction
from django.contrib.auth.models import User

class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = ['id', 'name', 'location', 'type']


class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = ['company', 'username', 'first_name', 'last_name', 'email']
    
  def create(self, validated_data):
    user_data = {
      'username': validated_data['username'],
      'email': validated_data['email'],
      'first_name': validated_data['first_name'],
      'last_name': validated_data['last_name'],
    }
    user = User.objects.create_user(**user_data)
    employee = Employee.objects.create(
      username = user,
      company = validated_data['company'],
      first_name = validated_data['first_name'],
      last_name = validated_data['last_name'],
      email = validated_data['email']
    )
    return employee
  

class DeviceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Device
    fields = ['id', 'name', 'description']


class TransactionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Transaction
    fields = ['id', 'employee', 'device', 'checked_out', 'checked_in', 'condition_on_checkout', 'condition_on_checkin']

