from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myApp.models import Administrator,User
from myApp.serializers import AdministratorSerializer,UserSerializer



"""version 1 of creating a view"""


@csrf_exempt
def Log_In_admin(request,username,password):
    
    try:
        administrator = Administrator.objects.get(pk=username)
    except Administrator.DoesNotExist :
        return HttpResponse("Administrator does not exist",status=401)

        



    if request.method == 'GET':
        adminserializer = AdministratorSerializer(administrator)
        
        
        
        if adminserializer.data['password']==password:
            return JsonResponse({'data':adminserializer.data,
            'type':'administrator'},status=200)

    
    return HttpResponse("password incorrect",status=401)
        





@csrf_exempt
def Log_In_user(request,username,password):
    
    try:
        user = User.objects.get(pk=username)
    except User.DoesNotExist :
        return HttpResponse("User does not exist",status=401)

        



    if request.method == 'GET':
        userserializer = UserSerializer(user)
        
        
        
        if  userserializer.data['password']==password:
            return JsonResponse({'data':userserializer.data,
            'type':'user'},status=200)

    
    return HttpResponse("password incorrect",status=401)