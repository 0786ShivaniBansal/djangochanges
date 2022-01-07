from os import name
from django.urls import path
from .import views
urlpatterns = [
    path('',views.resto, name='resto'),
    path('index',views.index, name='index'),
    path('fruits',views.fruits ,name='fruits'),
    path('user',views.user ,name='user'),
]

app_name='polls'