from django.shortcuts import render
from django.shortcuts import redirect, render
from accounts.models import Register,Login
from django.contrib.auth.models import User, auth


# Create your views here.
def register(request):
    if(request.method=='POST'):
        print(request.POST)
        r=Register.objects.create(firstname=request.POST['firstname'],rid=request.POST['rid'],emailid=request.POST['emailid'],passcode=request.POST['passcode'])
        return redirect('login')
    return render(request,('register.html'))


def login(request):
    if (request.method=='POST'):
        print(request.POST['username'])
        username=request.POST
        password=request.POST

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print("invalid credentials")
            return redirect('login')
    else:
        return render(request,('login.html'))


