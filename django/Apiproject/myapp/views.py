from django.shortcuts import render
import requests

# Create your views here.


def home(request):
    url="https://restcountries.com/v3.1/all"
    req=requests.get(url)
    d=req.json()
    print(d)
    return render(request,'home.html',{'d':d})



def ser(request,name):
     url="https://restcountries.com/v3.1/all"
     req=requests.get(url)
     d=req.json()
     if request.method=='POST':
        sa=request.POST['Region']
        print(sa)
        if sa in url:
           if d==sa:
               print(sa)
           else:
               print("error")

        