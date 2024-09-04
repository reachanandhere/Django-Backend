from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', '/advocates/:username']
    return Response(data)

@api_view(['GET'])
def advocates(request):
    data = ['Anand', 'Subhashini', 'Saravanan']
    return Response(data) 

@api_view(['GET'])
def advocate_detail(request, username):
    data = username
    return Response(data)
