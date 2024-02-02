from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
      path('add_student/',views.add_student , name='add_student'),
      path('remove_student/<int:id>',views.remove_student, name='remove_student'),
      path('remove_student/',views.remove_student),
       path('update_student/',views.update_student , name='update_student'),
          path('update_student/<int:id>',views.update_student , name='update_student'),
            path('show_student/',views.show_student, name='show_student'),
            path('userlogout/',views.userlogout),
             
]