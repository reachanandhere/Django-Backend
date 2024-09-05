from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from .models import Advocate

from .serializers import AdvocateSerializer

@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', '/advocates/:username']
    return Response(data)

@api_view(['GET', 'POST'])
def advocates(request):

    if request.method == 'GET':
        query = request.GET.get('query')
        if query == None:
            query = ''
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data) 

    if request.method == 'POST':
        data = request.data
        advocate = Advocate.objects.create(
            username = data['username'],
            bio = data['bio']
        )
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

@api_view(['GET'])
def advocate_detail(request, username):
    advocate = Advocate.objects.get(username=username)
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)
