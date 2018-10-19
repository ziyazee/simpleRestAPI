# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Student
from .serializers import serialize
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

# Create your views here.
class StudentList(APIView):

    #function call for get request
    def get(self,request,name):
        student=Student.objects.filter(name=name)
        serializer=serialize(student,many=True)
        return Response(serializer.data)

    #function call for [pst] request
    def post(self,request,name):
        serializer = serialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
