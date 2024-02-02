from django.shortcuts import render
from .form import *

# Create your views here.




def index(request):
    '''if request.method=='POST':
        form=displayform(request.POST,request.FILES)
        if  form.is_valid():
            form.save()
        else:
            print("erro")
    form=displayform'''
    img=product_sub_cat.objects.all()
    return render(request,'index.html',{'img':img})