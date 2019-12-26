from django.shortcuts import render,redirect,HttpResponse
from . import forms
from  django.contrib import messages
#create your views here

def register(request):
    if request.method=="POST":
        form=forms.UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Welcome to Traffic_prediction ...You are successfully registered!!')
            return redirect('login')

    else:
        #for the first time
        form=forms.UserCreateForm()
        context={"form":form}
        return render(request,"accounts/signup.html",context)
