from django.shortcuts import render

from django.shortcuts import render
from .models import Restaurent

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
def reservation(request):
    return render(request,'reservation.html')

