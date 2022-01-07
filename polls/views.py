from os import name
from django.shortcuts import redirect, render
from django.urls.conf import path
from .models import Login, Restaurent, Fruits, User,Login
from django.contrib.auth.models import auth

# Create your views here.
def index(request):
    rests=Restaurent.objects.all()
    return render(request,'index.html',{'rests':rests})


def resto(request):
    if(request.method=='POST'):
        print(request.POST)
        print(request.POST['name'],request.POST['descr'],request.POST['price'])
        r=Restaurent.objects.filter(name=request.POST['name'])
        if not r.exists():
            r=Restaurent.objects.create(name = request.POST['name'], descr = request.POST['descr'],price = request.POST['price'])
        else:
                print("name already exists")


    return render(request,'polls/resto.html')

def fruits(request):
    if(request.method=='POST'):
        print(request.POST)
        f=Fruits.objects.create(name=request.POST['name'],color=request.POST['color'],price=request.POST['price'])
    return render(request,('polls/fruits.html'))


def user(request):
    if(request.method=='POST'):
        print(request.POST)
        print(request.POST['username'])
        u=User.objects.create(username=request.POST['username'],id=request.POST['id'],Mobile=request.POST['Mobile'],Email=request.POST['Email'],Password=request.POST['Password'],Admin=request.POST['Admin'],Chef=request.POST['Chef'],Waiter=request.POST['Waiter'])
    
    return render(request,('polls/user.html'))

def login(request):
    if (request.method=='POST'):
        print(request.POST['username'])
        l=Login.objects.create(username=request.POST['username'],password=request.POST['password'])
        u=auth.authenticate()
        if login is not None:
            auth.login(request,id)
            return redirect('/')
        else:
            print("invalid credentials")
            return redirect('login')

    return render(request,('polls/login.html'))
