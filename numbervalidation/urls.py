from django.contrib import admin
from django.urls import path
from numbervalidation import urls, views

urlpatterns = [
    path("login/",views.login,name='login'),
     path("",views.register,name='login'),
    path('otp/<number>',views.otp),
    path('otp/sucess/',views.sucess,name='sucess')
]