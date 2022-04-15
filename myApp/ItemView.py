from pickle import FALSE
from django.http import JsonResponse
from myApp.models import Image, Item
from myApp.serializers import  ItemSerializer,ImageSerializer
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from collections import namedtuple
import json


"""version 2 of creating a view"""
class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer



@csrf_exempt
def Full_item(request,pk):
    if request.method == 'GET':
        images = Image.objects.filter(itemId=pk)
        imageSerializer = ImageSerializer(images, many=True)
        item=Item.objects.get(pk=pk)
        itemSerializer=ItemSerializer(item)
        return JsonResponse({"item":itemSerializer.data,
        "images":imageSerializer.data})





@csrf_exempt
def All_full_items(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        data={"items":[]}
       
        for item in serializer.data:
            images = Image.objects.filter(itemId=item['id'])
            imageSerializer = ImageSerializer(images, many=True)
            item=Item.objects.get(pk=item['id'])
            itemSerializer=ItemSerializer(item)
            data["items"].append({"item":itemSerializer.data,
            "images":imageSerializer.data})
            

        myResponse=json.dumps(data)
        return JsonResponse(data, safe=False)