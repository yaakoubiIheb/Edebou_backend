from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

class User(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=100,blank=False)
    lastName = models.CharField(max_length=30,blank=False)
    FirstName = models.CharField(max_length=30,blank=False)
    email = models.EmailField(max_length=50,blank=False)
    phone = models.CharField(max_length=20,blank=False)
    location = models.CharField(max_length=40,blank=False)
    def __str__(self):
        return self.username
    







class Item(models.Model):
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(blank=False)
    category = models.CharField(max_length=30,blank=False)
    price = models.DecimalField(max_digits=12, decimal_places=3)
    state = models.BooleanField(default=True)
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    emplacement=models.CharField(max_length=100,default="tunis")
    uploadDate = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title




class Report(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=False,default="issue")
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    state = models.BooleanField(default=True)
    def __str__(self):
        return self.title



class Image(models.Model):
    itemId = models.ForeignKey(Item,on_delete=models.CASCADE)
    imageData=models.TextField(blank=False)
    def __int__(self):
        return self.itemId

    