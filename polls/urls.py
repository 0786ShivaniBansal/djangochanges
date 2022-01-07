from os import name
from django.urls import path
from .import views
urlpatterns = [
    path('',views.resto, name='resto'),
    path('index',views.index, name='index'),
    path('fruits',views.fruits ,name='fruits'),
    path('user',views.user ,name='user'),
    path('login',views.login ,name='login')

]

app_name='polls'