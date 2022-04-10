from myApp.models import User
from myApp.serializers import UserSerializer
from rest_framework import generics

"""version 2 of creating a view"""
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer