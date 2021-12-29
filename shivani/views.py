from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def forms(request):
    return render(request,('forms.html'))
def add(request):
    sum1=int(request.GET["integer1"])
    sum2=int(request.GET["integer2"])
    dis = sum1 + sum2
    return render(request,"display.html",{"display":dis})
    
