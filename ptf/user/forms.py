# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.db import transaction
# from .models import *

# class UserRegisterForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model=User
#         fields='__all__'

#     @transaction.atomic
#     def save(self):
#         user=super().save(commit=False)
#         user.is_manager=True
#         user.save()
#         return user
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction 
 

class User_Registraion_Form(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        fields=('username','email','password1','password2')
    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.vendor=True
        user.save()
        return user 
    
class Buyer_Registraion_Form(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        fields=('username','email','password1','password2')
    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.customer=True
        user.save()
        return user    

class contactus_form(forms.ModelForm):
    class Meta:
        model =Contactus
        fields ='__all__'

class contactbuyForm(forms.ModelForm):
    class Meta:
        model = contactbuy
        fields ='__all__'


class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields ='__all__'
