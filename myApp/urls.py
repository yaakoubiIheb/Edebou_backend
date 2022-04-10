from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myApp.AdministratorView import Administrator_list,Administrator_detail
from myApp.ItemView import Full_item, ItemDetail, ItemList
from myApp.ImageView import*
from myApp.UserView import*
from myApp.loginView import*


urlpatterns = [
    path('administrator/',Administrator_list),
    path('administrator/<slug:pk>/',Administrator_detail),
    

    path('user/', UserList.as_view()),
    path('user/<slug:pk>/', UserDetail.as_view()),


    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
    path('fullItem/<int:pk>/', Full_item),
    


    path('report/', ItemList.as_view()),
    path('report/<int:pk>/', ItemDetail.as_view()),


    path('image/<int:pk>/',Image_details),
    path('image/', ImageView.as_view(), name= 'images_list'),



    path('login/admin/<slug:username>/<slug:password>/',Log_In_admin),
    path('login/user/<slug:username>/<slug:password>/',Log_In_user),
    
]