from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myApp.models import User
from myApp.serializers import UserSerializer

        





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