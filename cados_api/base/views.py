from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Advocate

from .serializers import AdvocateSerializer

@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', '/advocates/:username']
    return Response(data)

@api_view(['GET'])
def advocates(request):
    # data = ['Anand', 'Subhashini', 'Saravanan']
    advocates = Advocate.objects.all()
    serializer = AdvocateSerializer(advocates, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def advocate_detail(request, username):
    data = username
    return Response(data)
