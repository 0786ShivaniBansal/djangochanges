from unicodedata import name
from django.urls import path
from .import views
urlpatterns = [
     path('',views.index ,name='index'),
    path('register',views.register, name='register'),
    path('login',views.login , name='login'),
    path('web',views.web ,name='web'),
    path('submit',views.submit,name='submit'),
    path('dishes',views.dishes,name='dishes'),
    path('about',views.about,name='about')
]

app_name='accounts'