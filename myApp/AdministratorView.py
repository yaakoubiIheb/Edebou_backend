from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myApp.models import Administrator
from myApp.serializers import AdministratorSerializer



"""version 1 of creating a view"""


@csrf_exempt
def Administrator_list(request):
    """
    List all administrators, or create a new administrator.
    """
    if request.method == 'GET':
        administrators = Administrator.objects.all()
        serializer = AdministratorSerializer(administrators, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdministratorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)








@csrf_exempt
def Administrator_detail(request, pk):
    """
    Retrieve, update or delete an administrator.
    """
    try:
        administrator = Administrator.objects.get(pk=pk)
    except Administrator.DoesNotExist:
        return HttpResponse("Administrator not found",status=404)

    if request.method == 'GET':
        serializer = AdministratorSerializer(administrator)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AdministratorSerializer(administrator, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        administrator.delete()
        return HttpResponse("Administrator deleted successfully",status=204)