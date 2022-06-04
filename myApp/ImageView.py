from django.urls import Resolver404
from myApp.models import Image
from myApp.serializers import ImageSerializer
from rest_framework import generics

"""version 2 of creating a view"""

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer



class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer