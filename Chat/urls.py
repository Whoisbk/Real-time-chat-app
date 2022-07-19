from django.urls import path 
from . import views

urlpatterns = [
    path('',views.main, name ='main'),
    path('<str:lobby_name>/',views.lobby, name ='lobby'),
]
