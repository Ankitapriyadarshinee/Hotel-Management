import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum



class HotelCategory(models.Model):
    category_name = models.CharField(max_length=100)





class Hotel(models.Model):
    category = models.ForeignKey(HotelCategory ,on_delete=models.CASCADE ,related_name='hotels')
    hotel_name = models.CharField(max_length=100)
    price = models.IntegerField()
    images=models.ImageField(upload_to='hotel')
    check_in=models.DateTimeField(auto_now_add=False)
    check_out=models.DateTimeField(auto_now_add=False)
    Adult=models.IntegerField()
    children=models.IntegerField()

def __str__(self):
    return self.hotel_name



    