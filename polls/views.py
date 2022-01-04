from os import name
from django.shortcuts import render
from django.urls.conf import path
from .models import Restaurent, Fruits

# Create your views here.
def index(request):
    rest1 = Restaurent()
    rest1.name='PavBhaji'
    rest1.img='pav.jpg'
    rest1.descr='PAVBHAJI is special indian recipe served with a onions butter have a tasty and delightful flavour'
    rest1.price=700
    rest1.offer= False
    rest2=Restaurent()
    rest2.name='Pasta'
    rest2.img='chef-2.jpg'
    rest2.price=30
    rest2.discr='this is italian dish which is garnished with coriander served with various sauces'
    rest1.offer=False
    rests=[rest1,rest2]
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
    if (request.method=='POST'):
        print(request.POST)
        u=user.objects.create(username=request.POST['username'],id=request.POST['id'],Mobile=request.POST['Mobile'],Email=request.POST['Email'],Password=request.POST['Password'],Admin=request.POST['Admin'])
    
    return render(request,('polls/user.html'))
