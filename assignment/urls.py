from django.urls import path
from .import views

urlpatterns=[
    path('',views. register ,name='reg'),
    path('log',views.login ,name='log'),
    path('sub',views.sub,name='sub')
    
]
