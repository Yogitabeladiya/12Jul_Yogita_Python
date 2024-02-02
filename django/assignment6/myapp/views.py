from django.shortcuts import render
from .serailizers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from rest_framework import status

# Create your views here.


@api_view(["GET"])
def get(request):
    if request.method == "GET":
        stdata = Book.objects.all()
        serail = bookserailizers(stdata, many=True)
        return Response(serail.data, status=status.HTTP_202_ACCEPTED)


@api_view(["GET"])
def getid(request, id):
    try:
        stid = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial = bookserailizers(stid)
    return Response(data=serial.data)


@api_view(["GET", "DELETE"])
def deleteid(request, id):
    try:
        stid = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serial = bookserailizers(stid)
        return Response(data=serial.data)

    if request.method == "DELETE":
        Book.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def save(request):
    if request.method == "POST":
        stdata = bookserailizers(data=request.data)
        if stdata.is_valid():
            stdata.save()
            return Response(status=status.HTTP_202_ACCEPTED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["put", "GET"])
def updateid(request, id):
    try:
        stid = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == "GET":
        serial = bookserailizers(stid)
        return Response(data=serial.data)

    if request.method == "PUT":
        stdata = bookserailizers(data=request.data, instance=stid)
        if stdata.is_valid():
            stdata.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
