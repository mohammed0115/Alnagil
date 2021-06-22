from django.shortcuts import render

# Create your views here.
from .models import CustomUser
from .serializers import customUserSerializer,organizationUserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class userList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        customUser = CustomUser.objects.all()
        serializer = customUserSerializer(customUser, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = customUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)