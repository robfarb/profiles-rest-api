from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
  """Test Api View"""
  
  def get(self, request, format=None):
    """Returns a list of APIView features"""
    an_apiview = [
      'Uses HTTP methods as function (get, post, patch, put, delete)',
      'Is similar to a traditional Django view',
      'Gives you the most control over your applicatoon logic',
      'Is mapped manually to Urls',
    ]

    return Response({'message': 'Hello!', 'an_apiview': an_apiview})
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
