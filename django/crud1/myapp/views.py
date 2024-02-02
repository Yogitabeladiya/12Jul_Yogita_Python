from django.shortcuts import render,redirect
from .models import *
from .form import *

# Create your views here.


def Add_student(request):
    return render(request,'Add_student.html')


def Update_student(request):
    return render(request,'Update_student.html')


def Show_student(request):
    return render(request,'Show_student.html')

def index(request):
  '''  if request.method=='POST':
      if request.POST['signup']=='signup':
        user=studentinfoform(request.POST)
        if user.is_valid():
         user.save()
         print("signupsucess")
         return redirect('Add_student')
        else:
            print(user.errors)
    elif request.POST['login']=='login':
       unm= request.POSt['email']
       pas=request.POST['password']
       st=studentinfo.objects.filter(email=unm,passsword=pas)
       if st:
          print("login")
       else:
          print("error") 
    return render(request,'index.html')'''
  return render(request,'index.html')


'''def signup(request):
    if request.method=='POST':
        user=studentinfoform(request.POST)
        if user.is_valid():
         user.save()
         print("signupsucess")
        else:
            print(user.errors)
    return redirect('Add_student')'''