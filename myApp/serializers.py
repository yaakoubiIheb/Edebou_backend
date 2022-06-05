from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from myApp.models import User,Item,Image,Report


    
        








class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields ='__all__'







class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields =['id','title','description','category','price','state','seller','uploadDate']








class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Report
        fields =['id','username','title','item','description','state']










class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields =['id','itemId','imageData']




