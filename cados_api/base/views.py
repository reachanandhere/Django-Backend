from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Advocate, Company

from .serializers import AdvocateSerializer, CompanySerializer  

@api_view(['GET'])
def endpoints(request):
    data = ['/advocates', '/advocates/:username']
    return Response(data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
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

# @api_view(['GET', 'PUT', 'DELETE'])
# def advocate_detail(request, username):
#     advocate = Advocate.objects.get(Q(username=username))

#     if request.method == 'GET':
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         data = request.data  
#         advocate.username = data['username']
#         advocate.bio = data['bio']
#         advocate.save()
#         serializer = AdvocateSerializer(advocate, many=False)
#         return Response(serializer.data)

#     if request.method == 'DELETE':
#         advocate.delete()
#         return Response('user was deleted')

class Advocate_detail(APIView):
    def get(self, request, username):
        advocate = Advocate.objects.get(Q(username__icontains=username))
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def put(self, request, username):
        data = request.data
        advocate = Advocate.objects.get(Q(username=username))
        advocate.username = data['username']
        advocate.bio = data['bio']
        advocate.save()
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def delete(self, request, username):
        advocate = Advocate.objects.get(Q(username=username))
        advocate.delete()
        return Response('user was deleted')
    
@api_view(['GET'])
def companies_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)