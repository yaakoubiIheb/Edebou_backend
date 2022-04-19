from django.urls import Resolver404
from myApp.models import Report
from myApp.serializers import ReportSerializer
from rest_framework import generics

"""version 2 of creating a view"""
class ReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer