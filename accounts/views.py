from django.shortcuts import render
from django.shortcuts import redirect, render
from accounts.models import Register,Login, Web,pavbhaji
from django.contrib.auth.models import User, auth


# Create your views here.
def register(request):
    if(request.method=='POST'):
        print(request.POST)
        r=Register.objects.create(firstname=request.POST['firstname'],rid=request.POST['rid'],emailid=request.POST['emailid'],passcode=request.POST['passcode'])
        return redirect('/submit')
    return render(request,('register.html'))


def login(request):
    if (request.method=='POST'):
        print(request.POST['username'])
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/index')
        else:
            print("invalid credentials")
            return redirect('/register')
    else:
        return render(request,('login.html'))

        
# def logout(request):
#     auth.logout(request)
#     return redirect('/')


def index(request):
    return render(request,('index.html'))

def web(request):
    if(request.method=='POST'):
            print(request.POST)
            w=Web.objects.create(customername=request.POST['customername'],age=request.POST['age'],Address=request.POST['Address'],days=request.POST['days'],numdays=request.POST['numdays'])
            return redirect('/register')

    return render(request,('web.html'))


def submit(request):
    return render(request,'submit.html')


def dishes(request):
    if(request.method=='POST'):
        print(request.POST)
        p=pavbhaji.objects.create(order=request.POST['order'],price=request.POST['price'])
        return redirect('/submit')
    return render(request,'pavbhaji.html')


def about(request):
    return render(request,'about.html')