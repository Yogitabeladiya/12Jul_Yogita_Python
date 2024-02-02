from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('Add_student/',views.Add_student),
    path('Update_student/',views.Update_student),
    path('Show_student/',views.Show_student),
]
