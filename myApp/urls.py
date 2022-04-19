from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myApp.AdministratorView import Administrator_list,Administrator_detail
from myApp.ItemView import All_full_items, Full_item, ItemDetail, ItemList
from myApp.ImageView import*
from myApp.UserView import*
from myApp.loginView import*
from myApp.ReportView import*



urlpatterns = [
    path('administrator/',Administrator_list),
    path('administrator/<slug:pk>/',Administrator_detail),
    

    path('user/', UserList.as_view()),
    path('user/<slug:pk>/', UserDetail.as_view()),


    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
    path('fullItem/<int:pk>/', Full_item),
    path('items/', All_full_items),
    


    path('report/', ReportList.as_view()),
    path('report/<int:pk>/', ReportDetail.as_view()),


    path('image/<int:pk>/',Image_details),
    path('image/', ImageView.as_view(), name= 'images_list'),



    path('login/admin/<slug:username>/<slug:password>/',Log_In_admin),
    path('login/user/<slug:username>/<slug:password>/',Log_In_user),
    
]