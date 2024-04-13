from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company, Employee, Story, Transaction
from .serializers import CompanySerializer, EmployeeSerializer, StorySerializer, TransactionSerializer


class CreateCompanyAPI(APIView):
  def post(self, request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED, data=serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class ShowCompanyAPI(APIView):
  def get(self, request):
    companys = Company.objects.all()
    serializer = serializer_class = CompanySerializer(companys, many=True)
    return Response(status=status.HTTP_200_OK, data=serializer.data)

class CreateEmployeeAPI(APIView):
  def post(self, request):
    serializer = EmployeeSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class ShowEmployeeAPI(APIView):
  def get(self, request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
class CreateStoryAPI(APIView):
    def post(self, request):
      serializer = StorySerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ShowStoryAPI(APIView):
  def get(self, request):
    stories = Story.objects.all()
    serializer = StorySerializer(stories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
class CreateTransactionAPI(APIView):
    def post(self, request):
      serializer = TransactionSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ShowTransactionAPI(APIView):
  def get(self, request):
    devices = Transaction.objects.all()
    serializer = TransactionSerializer(devices, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)