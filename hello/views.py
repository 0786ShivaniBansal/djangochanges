from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, response
from hello.models import User

# Create your views here.
def base(request):
    return HttpResponse("hello world")
def home(request):
    return render(request,'home.html')


def add(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val1 + val2

    return render(request, "result.html",{"result": res})

def user(request):
    if (request.method=='POST'):
        print(request.POST)
    u=User.objects.create(idname=request.POST['idname'],firstname=request.POST['firstname'],lastname=request.POST['lastname'],companyname=request.POST['companyname'],age=request.POST['age'],city=request.POST['city'],state=request.POST['state'],zip=request.POST['zip'],email=request.POST['email'],web=request.POST['web'])
    return render(request,'user.html')


# def userdetails(request):
    
#     return render(request,'user.html')