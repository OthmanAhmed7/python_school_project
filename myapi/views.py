from django.shortcuts import render

from myapi.serializers import CategorySerializer
from .models import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many = True)

    return Response({'message': 'all categories', 'data': serializer.data}, status = HTTP_200_OK)