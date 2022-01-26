from attr import validate
from django.http import response
from rest_framework .views import APIView
from rest_framework .response import Response
from rest_framework import status
from .serailizers import *

class regapi(APIView):
    def get(self,request):
        model=Register.objects.all()
        serializer=register(model,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=register(data=request.data)
        if serializer. is_valid():
            return Response(serializer.data,status=status .HTTP_201_CREATED)
        return Response(serializer.errors,status=status .HTTP_400_BADREQUEST)