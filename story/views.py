from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Story
from .serializers import  StorySerializer
from rest_framework.generics import GenericAPIView
from .permissions import IsWriter
from rest_framework.permissions import IsAuthenticated
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
  

class IsWriterAPI(GenericAPIView):
  permission_classes = [IsWriter]
  def get(self, request):
    data = {
      "msg": "A request from a writer"
    }
    return Response(data, status=status.HTTP_200_OK)

class MakeWriterAPI(GenericAPIView):
  permission_classes = [IsAuthenticated]
  def get(self, request):
    user = request.user
    user.is_writer = True
    user.save()
    return Response({'message': 'User is now a writer'}, status=status.HTTP_200_OK)
