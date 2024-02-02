from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
  path('',views.get),
  path('getid/<int:id>',views.getid),
  path('deleteid/<int:id>',views.deleteid),
  path('save/',views.save),
  path('updateid/<int:id>',views.updateid),
]