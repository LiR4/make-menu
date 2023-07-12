from django.urls import path
from app_menu import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('menu/', views.Menu, name='Menu'),
]
