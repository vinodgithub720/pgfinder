from django import forms
from .models import *
from user.models import User


class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model =Property_info
        fields ='__all__'

class AddpropertyForm(forms.ModelForm):
    class Meta:
        model =Property_info
        fields ='__all__'
        
class ProjectTeamCreationForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter())
    
    class Meta:
        model =ProjectTeam
        fields ='__all__'