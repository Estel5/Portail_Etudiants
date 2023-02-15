from django.shortcuts import render
from django.views import View

def base_view(request,*args,**kwargs):
    return render(request, "tableauAcceuil/base.html")

def home_view(request,*args,**kwargs):
    return render(request,"tableauAcceuil/home.html", name='home')
