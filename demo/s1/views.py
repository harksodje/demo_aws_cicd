# from multiprocessing import dummy
# from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializer import userSerializer

# Create your views here.


class userlist(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):

        todos = User.objects.filter(user=request.user_name)
        serializer = userSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):

        data = {
            'user_name': request.data.get('user_name'),
            'email': request.data.get('email'),

        }
        serializer = userSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
