from django.shortcuts import render,redirect
from rest_framework import generics
from .models import *
from .serailizers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import requests
from rest_framework.views import APIView
from .forms import MyModelForm

# # Create your views here.


class Myview(APIView):

    @api_view(['GET'])
    def getdata(request,):
        if request.method=='GET':
            snippestdata=snippest.objects.all()
            serial=snippestserailizers(snippestdata,many=True)
            return Response(data=serial.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
  
        


class Myview1(APIView):
 @api_view(["GET"])
 def getid(request, id):
    try:
        stid = snippest.objects.get(id=id)
    except snippest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serial = snippestserailizers(stid)
    return Response(data=serial.data)


   




class MyModelListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = snippestserailizers

    def get_queryset(self):
        output_format = self.request.query_params.get('format')
        if output_format == 'html':
            form = MyModelForm()
            return form
        return snippest.objects.all()

    def create(self, request, *args, **kwargs):
        if request.content_type == 'application/x-www-form-urlencoded':
            form = MyModelForm(request.POST)
            if form.is_valid():
                form.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
