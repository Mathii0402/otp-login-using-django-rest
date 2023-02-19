from http.client import HTTPResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .mixins import meshandler
import random
from django.contrib.auth import login as auth_login
# Create your views here.
def login(request):
    if request.method =="POST":
        mobnumber=request.POST['number']
        profile = Profile.objects.get(mobnumber=mobnumber)
        if profile  is None:
            print("no user")
            return redirect("/")
        
        profile.otp = random.randint(1000,9999) 

        profile.save()
        print(profile.mobnumber)
        meshandle = meshandler(mobnumber,profile.otp).send_otp_on_mob()
        return redirect(f'/otp/{mobnumber}')
    
    return render(request,"login.html")
    

def register(request):
    if request.method =="POST":
        username=request.POST['username']
        mobnumber=request.POST['number']
        paswd=request.POST['pasw']
        if not User.objects.filter(username=username).exists():
            if not Profile.objects.filter(mobnumber=mobnumber).exists():
                user = User.objects.create(username=username)
                profile =Profile.objects.create(user=user,mobnumber=mobnumber)
                messages.success(request,"User registered!!!")
                return redirect("login/")
            else: 
                messages.warning(request,"Number already register!!!")
        else:
            messages.info(request,"User name taken!!!")
    return render(request,"register.html")
       

def otp(request,number):
    if request.method =="POST":
        otp = request.POST['otp']
        
        profile = Profile.objects.get(mobnumber=number)
        if otp == profile.otp:
            auth_login(request,profile.user)
            return redirect("sucess/")
        return redirect(f'/otp/{number}')
    return render(request,'otp.html') 

def sucess(request):
    return render(request,'success.html')