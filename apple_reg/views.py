from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Apple

# Create your views here.

@login_required(login_url = 'login')
def registration(request):
   if request.method == 'POST':
      year_of_production= request.POST['yop']
      breed = request.POST['breed']
      row = request.POST['row']
      column = request.POST['column']
      latitude = request.POST['latitude']
      longitude = request.POST['longitude']
      new_apple = Apple.objects.create(year_of_production=year_of_production, breed=breed, row=row, column=column, latitude=latitude, longitude=longitude)
      new_apple.save()
      return redirect('register')
   else:
      return render(request, 'register.html')


def login(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']

      user = auth.authenticate(username=username, password=password)

      if user is not None:
         auth.login(request, user)
         return redirect('register')
      else:
         messages.info(request, 'Credentials Invalid')
         return redirect('login')

   else:
      return render(request, 'login.html')
