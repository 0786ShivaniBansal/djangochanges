from django.urls import path
from django.urls.resolvers import URLPattern
from django .urls import path
from . import views
urlpatterns = [
    path('',views.forms,name="forms"),
    path('add',views.add,name="add"),
]