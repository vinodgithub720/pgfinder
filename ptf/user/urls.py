from django.contrib import admin
from django.urls import path,include
from .views import User_Registraion_View,Buyer_Registraion_View ,UserLogin1View,UserLoginView,contactus_view
from user import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required



urlpatterns = [
   
   path('adduser/',User_Registraion_View.as_view(),name='userregister'),
   path('register/',Buyer_Registraion_View.as_view(),name='buyer'),
   path('login/',UserLoginView.as_view(),name='login'),
   path('login1/',UserLogin1View.as_view(),name='login'),
   path('logout/',LogoutView.as_view(),name='logout'),
   path('sendmail/',views.sendMail,name='sendmail'),
   path('contactus/',contactus_view.as_view(),name='contact'),
   
]  