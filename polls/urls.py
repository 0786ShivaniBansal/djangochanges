from os import name
from django.urls import path
from .import views
urlpatterns = [
    path('',views.resto, name='resto'),
    path('index',views.index, name='index'),

]

app_name='polls'