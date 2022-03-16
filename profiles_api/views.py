from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
  """Test Api View"""
  seralizer_class = serializers.HelloSerializer
  
  def get(self, request, format=None):
    """Returns a list of APIView features"""
    an_apiview = [
      'Uses HTTP methods as function (get, post, patch, put, delete)',
      'Is similar to a traditional Django view',
      'Gives you the most control over your applicatoon logic',
      'Is mapped manually to Urls',
    ]

    return Response({'message': 'Hello!', 'an_apiview': an_apiview})

  def post(self, request):
    """Create a hello message with our name"""
    serializer = self.seralizer_class(data=request.data)
    
    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}'
      return Response({'message': message})
    else:
      return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
      )

  def put(self, request, pk=None):
    """
    Handle Updating an Object
    """
    return Response({'method': 'PUT'})


  def patch(self, request, pk=None):
    """
    Handle a partial update of an object
    """
    return Response({'method': 'PATCH'})

  
  def delete(self, request, pk=None):
    """
    Delete an object
    """
    return Response({'method': 'DELETE'})
        
class TestApiView(APIView):
  """Another Test Api View"""
  
  def get(self, request, format=None):
    """Returns a list of APIView features"""
    an_apiview = [
      'Test',
      'Test 2',
      10,
      {'test': 'apple'}
    ]

    return Response({'message': 'Hello!', 'an_apiview': an_apiview})

class HelloViewSet(viewsets.ViewSet):
  """
  Test API Viewset
  """
  serializer_class = serializers.HelloSerializer

  def list(self, request):
    """
    Return a hello message
    """
    a_viewset = [
      'User Actions', 
      'List', 
      'Retrieve', 
      'Automatically maps to URLS using Routers', 
      'Provides more functionality with less code',
    ]

    return Response({'message': 'Hello!', 'a_viewset': a_viewset})

  def create(self, request):
    """
    Creates a new a hello message
    """
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}!'
      return Response({"message": message})
    else:
      return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
      )


  def retrieve(self, request, pk=None):
    """
    Handle getting object by It's ID
    """
    
    return Response({'http_method': 'GET'})


class UserProfileViewset(viewsets.ModelViewSet):
  """
  Handle Creating and updating profiles
  """

  serializer_class = serializers.UserProfileSerializer
  queryset = models.UserProfile.objects.all()
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.UpdateOwnProfile,)