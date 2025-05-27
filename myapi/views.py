from django.shortcuts import render

from myapi.serializers import CategorySerializer, UserSerializer
from .models import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def users(request, id=None):
    if request.method == "GET":
        if id is not None:
            try:
                user = User.objects.get(id=id)
                serializer = UserSerializer(user)
                return Response({'message': 'User retrieved successfully', 'data': serializer.data}, status=HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'message': 'User not found'}, status=HTTP_404_NOT_FOUND)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response({'message': 'all users', 'data': serializer.data}, status=HTTP_200_OK)

    elif request.method == "POST":
        data=request.data
        data['password']=make_password(data['password'])
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'user created successfully', 'data': serializer.data}, status = HTTP_201_CREATED)

        return Response({'message': 'wrong in creation', 'data': serializer.errors}, status = HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'user updated successfully', 'data': serializer.data}, status=HTTP_200_OK)
            return Response({'message': 'error in updating user', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'message': 'user not found'}, status=HTTP_404_NOT_FOUND)
        
    elif request.method == "DELETE":
        try:
            user = User.objects.get(id=id)
            user.delete()
            return Response({'message': 'user deleted successfully'}, status=HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'message': 'user not found'}, status=HTTP_404_NOT_FOUND)


@api_view(['GET'])
def login(request):
    data=request.data
    try:
        user=User.objects.get(email=data['email'])
        if user and check_password(data['password'], user.password):
            return Response({'message':'user login successfully'}, status=HTTP_200_OK)
        return Response({'message':'wrong username or password'}, status=HTTP_404_NOT_FOUND)
    except:
        return Response({'message':'wrong username or password'}, status=HTTP_404_NOT_FOUND)
    
class CategoryView(APIView):
    def get(self, request, id=None):
        if id is not None:
            try:
                category = Category.objects.get(id=id)
                serializer = CategorySerializer(category)
                return Response({'message': 'category retrieved successfully', 'data': serializer.data}, status=HTTP_200_OK)
            except Category.DoesNotExist:
                return Response({'message': 'category not found'}, status=HTTP_404_NOT_FOUND)
        else:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response({'message': 'all categories', 'data': serializer.data}, status=HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'category created successfully', 'data': serializer.data}, status=HTTP_201_CREATED)
        return Response({'message': 'error in creation', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        try:
            category = Category.objects.get(id=id)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'category updated successfully', 'data': serializer.data}, status=HTTP_200_OK)
            return Response({'message': 'error in updating category', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response({'message': 'category not found'}, status=HTTP_404_NOT_FOUND)
        
    def delete(self, request, id=None):
        try:
            category = Category.objects.get(id=id)
            category.delete()
            return Response({'message': 'category deleted successfully'}, status=HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({'message': 'category not found'}, status=HTTP_404_NOT_FOUND)