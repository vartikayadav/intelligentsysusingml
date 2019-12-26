from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from insert_data.models import Data
from django.contrib import messages
from django.conf import settings
from . import views
from . import hackathon

# Create your views here.

def pred(request):
    detail=Data.objects.all()

    f=hackathon.fun()
    fit_data=f[0]
    pred_data=f[1]
    return render(request,"predict/predict.html",{"detail":detail,"fit_data":fit_data,"pred_data":pred_data})

def graph(request):
    f1=hackathon.fun()
    g=f1[2]
    return render(request,"predict/prediction2.html",{"g":g})
