from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

#Create your models here.

User = get_user_model()

class Profile(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    
    def __str__ (self):
       return self.user.username
    
    
class Apple(models.Model):
    year_of_production = models.IntegerField()
    breed = models.CharField(max_length=100)
    row = models.IntegerField()
    column = models.IntegerField()
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

    def __str__(self):
        return self.breed

   # def get_absolute_url(self):
    #    return reverse('apple_register', {'pk': self.pk})
    
