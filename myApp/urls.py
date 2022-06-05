from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myApp.ItemView import*
from myApp.ImageView import *
from myApp.UserView import*
from myApp.loginView import*
from myApp.ReportView import*



urlpatterns = [
    
    

    path('user/', UserList.as_view()),
    path('user/<slug:pk>/', UserDetail.as_view()),


    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
    path('fullItem/<int:pk>/', Full_item),
    path('items/', All_full_items),
    


    path('report/', ReportList.as_view()),
    path('report/<int:pk>/', ReportDetail.as_view()),

    
    path('image/', ImageList.as_view()),
    path('image/<int:pk>/', ImageDetail.as_view()),
    


    
    path('login/user/<slug:username>/<slug:password>/',Log_In_user),
    
]