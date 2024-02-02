from django.shortcuts import render,redirect
from .form import *
from .models import *
from django.contrib.auth import logout


# Create your views here.


def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            user=studentform(request.POST)
            if user.is_valid():
                user.save()
                print("signup sucess")
            else:
                print(user.errors)
        elif request.POST.get('login')=='login':
           unm=request.POST['username']
           pa=request.POST['password']
           user=student.objects.filter(username=unm,password=pa)
           if user:
              print("loginn")
              request.session['user']=unm
              return redirect('add_student')
           else:
              print("eroor")
    return render(request,"index.html")



def userlogout(request):
    logout(request)
    return redirect('/')




def add_student(request):
    user=request.session.get('user')
    if request.method=='POST':
            user=studentform(request.POST)
            if user.is_valid():
                user.save()
                print("added")
                return redirect('show_student')
            else:
                print(user.errors)
    return render(request,"add_student.html",{'user':user})



def update_student(request,id=0):
    st=student.objects.get(id=id)
    if request.method=='POST':
        user=studentform(request.POST,instance=st)
        if user.is_valid():
            user.save()
            print("updated sucessfully")
            return redirect('show_student')
        else:
            print(user.errors)

    return render(request,'update_student.html',{'st':st})




def remove_student(request,id=0):
    st=student.objects.get(id=id)
    student.delete(st)
    return redirect('show_student')


def show_student(request):
    user=request.session.get('user')
    stu=student.objects.all()
    return render(request,'show_student.html',{'user':user,'stu':stu})

