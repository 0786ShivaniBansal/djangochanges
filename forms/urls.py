from django.urls import path
from .import views
urlpatterns = [
    path('addition',views.addition,name="addition")
]