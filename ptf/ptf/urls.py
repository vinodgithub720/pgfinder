"""ptf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from user import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
   
    path('',home),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('property/', include('property.urls')),
    path('aboutus/',aboutus),
    path('Contactbuy/',contactbuyView.as_view(),name='contact_buy'),
     path('Rent/',RentView.as_view(),name='rent_amount'),
    path('properties/',property),
    path('payment/',payment),
    path('profile/',profile),
    path('testimonials/',testimonials), 
    path('success/',sucessfull),
    path('search/',login_required(views.search),name='search'),
    path('search1/',login_required(views.search1),name='search1'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)