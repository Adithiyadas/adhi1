from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    userName=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput())
    
class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']




