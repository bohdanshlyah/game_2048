from django.urls import path
from . import views

urlpatterns = [
    path('new', views.main, name="main"),
]