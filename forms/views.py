from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def addition (request):
    val1=int(request.GET["a1"]),
    val2=int(request.GET["a2"]),
    res=val1+val2


    return render(request,"result.html",{"result":res})