from django.contrib import admin
from django.urls import path,include
from myfile import views

urlpatterns = [
    path('',views.upload,name='upload'),
    

]
