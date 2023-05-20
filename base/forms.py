from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#importing the database modules for the user 
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username= forms.CharField(widget=forms.TextInput(attrs=
        {'placeholder':'Your username',
         'class':'w-full py-4 px-6 rounded xl'
         }))   
    password= forms.CharField(widget=forms.PasswordInput(attrs=
        {'placeholder':'Your Password',
         'class':'w-full py-4 px-6 rounded xl'
         }))  
    



class SignupForm(UserCreationForm):
    #including some configurations
    class Meta:
        model=  User
        fields = ('username','email','password1','password2')#password 2 is the repeat the confirmaation password
        #we import the for we created to views
    
    username= forms.CharField(widget=forms.TextInput(attrs=
        {'placeholder':'Your username',
         'class':'w-full py-4 px-6 rounded xl'
         }))   
    
    email= forms.CharField(widget=forms.EmailInput(attrs=
        {'placeholder':'Your Email Address',
         'class':'w-full py-4 px-6 rounded xl'
         })) 
    password1= forms.CharField(widget=forms.PasswordInput(attrs=
        {'placeholder':'Your Password',
         'class':'w-full py-4 px-6 rounded xl'
         }))    
          
    password2= forms.CharField(widget=forms.PasswordInput(attrs=
        {'placeholder':'Repeat password',
         'class':'w-full py-4 px-6 rounded xl'
         }))                            