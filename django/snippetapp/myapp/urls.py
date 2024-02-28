from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [

 #path('',views.save),
 path('getdata/',Myview.getdata),
 path('getid/<int:id>',Myview1.getid),
 path('my-models/', MyModelListCreateAPIView.as_view(), name='my-model-list'),
]