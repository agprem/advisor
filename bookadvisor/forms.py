# forms.py
from django import forms
from django.forms import ModelForm

from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from bookadvisor .models import UserTest
from bookadvisor .models import Advisor
from django.core.exceptions import ValidationError


#FORM FOR ADVISOR CREATION---------------------
class Advisorform(forms.ModelForm):

    class Meta:
        model = Advisor
        fields = ["first_name","profilepic"]
    def clean(self):
        first_name=self.cleaned_data['first_name']
        #("Hello",first_name)
        if (first_name==""):
            #print("inside val",first_name)
            raise forms.ValidationError("!!!  ADVISOR MUST HAVE SOME NAME !!!!")


#FORM FOR USER REGISTRATION--------------------------------------------------
class RegistrationForm(forms.ModelForm):
    #email = forms.EmailField(max_length = 60, help_text='Required, Add a Valid email')

    class Meta:
        model = UserTest
        fields = ("name","email","password")

#FORM FOR AUTHENTICATION OF USER---------------------------------------------------------
class CustomUserAuthenticationForm(forms.ModelForm):

    #password = forms.CharField(label='password',widget=forms.PasswordInput)

    class Meta:
        model = UserTest
        fields = ('email','password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        #print("after cleaned data")
        #print(email,password)
        if not authenticate(email = email, password=password):
            #print(email,password)
            #print("Not authenticated")
            raise forms.ValidationError('Invalid Login')
