from django.forms import models
from django.http import response
from rest_framework .views import APIView
from rest_framework .response import Response
from . serailizer1 import *
from hello import serailizer1
from rest_framework import status


class apiuser(APIView):
    def get(self,request):
        model=User.objects.all()
        serailizer1=userserializer(model,many=True)
        return Response(serailizer1.data,status=status.HTTP_200_OK)
        


    def post(self,request):
        serializer1=userserializer(data=request.data)
        if serializer1.is_valid():
            return response(serializer1.data,status=status.HTTP_201_CREATED)
        return response(serializer1.errors,status=status.HTTP_400_BAD_REQUEST)


class userdetails(APIView):

    def get_User(self,idname):
        try:
            model=User.objects.get(idname=idname)
            return model
        except:
            return Response("user not found ")
    def get(self,request,idname):
         serailizer1=userserializer(self.get_User(idname))
         return Response(serailizer1.data,status=status.HTTP_200_OK)
        


    def put(self,request,idname):
        serializer1=userserializer(self.get_User(idname),data=request.data)
        if serializer1.is_valid():
            serailizer1.save()
            return Response(serializer1.data,status=status.HTTP_201_CREATED)
        return Response(serializer1.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,idname):
        model=self.get_User(idname)
        model.delete
        return Response(status=status.HTTP_204_NO_CONTENT)
    