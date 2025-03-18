from django import forms
from django.contrib.auth.models import User

class loginform(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
class signupform(forms.ModelForm):
    class meta:
        model=User
        fields=['username','email','password','first_name','last_name']