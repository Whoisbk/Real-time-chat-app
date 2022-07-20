from django.urls import path 
from . import views

urlpatterns = [
    path('',views.main, name ='main'),
    path('signin/',views.signin, name ='signin'),
    path('register/',views.register, name ='register'),
    path('<str:lobby_name>/',views.lobby, name ='lobby'),
    
    
]
