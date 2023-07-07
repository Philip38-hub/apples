from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name='register'),
    path('login', views.login, name='login')
]