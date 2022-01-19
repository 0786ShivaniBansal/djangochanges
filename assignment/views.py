
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django .http import HttpResponse

from assignment.models import reg,login

# Create your views here.
def register(request):
    if(request.method=='POST'):
        print(request.POST)
        r=reg.objects.create(Name=request.POST['Name'],email=request.POST['email'],DOB=request.POST['DOB'],phoneNumber=request.POST['phoneNumber'])
    return render(request,'reg.html')



def login(request):
    if(request.method=='POST'):
        print(request.POST['username'])
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            
        else:
            print("invalid credentials")
            return redirect('/sub')
    return render(request,'log.html')

def sub(request):
    return render(request,'submit.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
   
    

        