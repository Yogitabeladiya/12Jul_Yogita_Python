from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.


def home(request):
    if request.method=='POST':
        form=imageform(request.POST,request.FILES)
        if  form.is_valid():
            form.save()
        else:
            print("erro")
    form=imageform
    img=Image.objects.all()
    return render(request,'home.html',{'form':form,'img':img})