from django.http import JsonResponse
from .serializers import ImageSerializer
from .models import Image
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        images_serializer = ImageSerializer(data=request.data)
        if images_serializer.is_valid():
            images_serializer.save()
            return Response(images_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', images_serializer.errors)
            return Response(images_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@csrf_exempt
def Image_details(request,pk):
    """
    List all images, or create a new Image.
    """
    if request.method == 'GET':
        images = Image.objects.filter(itemId=pk)
        serializer = ImageSerializer(images, many=True)
        return JsonResponse(serializer.data, safe=False)