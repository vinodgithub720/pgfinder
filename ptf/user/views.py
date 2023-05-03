# from django.shortcuts import render
# from .models import User
# from django.http import HttpResponse
# from django.views.generic import CreateView
# from .forms import UserRegisterForm
# from django.contrib.auth import login
# from django.contrib.auth.views import LoginView
# from django.urls import reverse_lazy
# from django.views.generic import TemplateView



# Create your views here.
 # def addUser(request):
    
 #     form = UserRegisterForm()
 #     if request.method == "POST":
 #         form = UserRegisterForm(request.POST or None)
 #         if form.is_valid():
 #             form.save()
 #         return HttpResponse("User registered")  
          
        
    # return render(request,'user/adduser.html',{'form':form})

# class UserregisterView(CreateView):
#     model=User
#     form_class=UserRegisterForm
#     template_name='user/user_register.html'
#     success_url='/'


# class Userloginview(LoginView):
#     template_name='user/login.html'
#     success_url='/'

#     def get_redirect_url(self):
#         if self.request.user.is_authenticated:
#             if self.request.user:
#                 return '/owner/'
#             else:
#                 return '/customer/'
        
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from property.models import *
from .forms import *
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.http import HttpResponse , HttpResponseRedirect
from django.views.generic import ListView
from .models import *
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.
class User_Registraion_View(CreateView):
     model = User
     form_class = User_Registraion_Form
     template_name = 'user_register.html'
     success_url = '/' 
     
    
    
    
     def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
     
     


class Buyer_Registraion_View(CreateView):
    model = User
    form_class = Buyer_Registraion_Form
    template_name = 'user_register.html'
    success_url = '/user/sendmail/'

   
    def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    
   

class UserLoginView(LoginView):
    template_name = 'login.html'
    success_url='/'
    
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user:
                return '/property/list_project1/'
            else:
                return HttpResponse("invalid username or password")

# class LogoutView(LogoutView):
    # def get(self, request):
    #     logout(request)
    #  return HttpResponse("you are logged out")
        # return HttpResponseRedirect(settings.LOGIN_URL)

class UserLogin1View(LoginView):
    template_name = 'login1.html'
    success_url='property/create_project/'
    
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user:
                return '/property/create_project/'
            else:
                return HttpResponse("invalid username or password")

    
class UserLogoutView(LogoutView):
   def get(self,request):
        logout(request)
        return redirect('/user/login')

def home(request):
    return render(request,'property/index.html')  #making the first page


def aboutus(request):
    return render(request,'property/about.html')

class contactbuyView(CreateView):
    form_class =contactbuyForm
    model = contactbuy
    template_name = 'contactbuy.html'
    success_url = '/'
    

# def contactus(request):
#     return render(request,'property/contact.html')

def property(request):
    return render(request,'property/properties.html')

def testimonials(request):
    return render(request,'property/testimonials.html')

def payment(request):
    return render(request,'property/payment.html' )

def sucessfull(request):
    return render(request,'sucessfull.html' )

def profile(request):
    return render(request,'userprofile.html' )
# send_mail (
#             'property finnder',
#             'thank you for choosing us...',
#             'imrankhanbaloch811@gmail.com',
#             ['imrankhanbaloch811@gmail.com'],
            
#             fail_silently=False,
#     )  
# 


def sendMail(request):
    subject = "welcome to PG finder"
    message = "hello new user , thanks for choosing us, find pg like home with us "
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['vinodkumavat154@gmail.com']
    res = send_mail(subject,message,email_from,recipient_list)
    if res>0:
        # print("mail sent")
        return render(request,'login.html')
    else:
        print("mail not sent")    
    print(res)
    return HttpResponse("mail sent")


class contactus_view(CreateView):
     model = Contactus
     form_class = contactus_form
     template_name = 'property/contact.html'
     success_url = '/'


class RentView(CreateView):
    form_class =RentForm
    model = Rent
    template_name = 'rent.html'
    success_url = '/'

def search(request):
    query = request.GET['query']
    # alllist = Property_info.objects.all()
    alllist = Property_info.objects.filter(name__icontains=query)
    params = {'project_list1': alllist}
    return render(request, "search.html" , params)

def search1(request):
    query1 = request.GET['query1']
    # alllist = Property_info.objects.all()
    alllist = Property_info.objects.filter(owners_name__icontains=query1)
    params = {'project_list': alllist}
    return render(request, "search1.html" , params)