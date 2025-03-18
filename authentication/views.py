from django.shortcuts import render,redirect
from authentication.forms import loginform,signupform
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.

def login_page(request):
 if request.method=='GET':
    lg_form=loginform()
    context={
        'form':lg_form
    }
    return render(request,'login.html',context)
 else:
    lg_form=loginform(request.POST)
    if lg_form.is_valid():
     username=lg_form.cleaned_data["username"]
     password=lg_form.cleaned_data["password"]
     user=authenticate(request,username=username,password=password)
     if user:
         login(request,user)
         return redirect("/students")
 messages.error(request,f'Invalid username or password')
 context={
         'form':lg_form
     }
 return render(request,'login.html',context)

def signup_page(request):
       if request.method=='POST':
        sg_form=signupform(request.POST)
        if sg_form.is_valid():
            sg_form.save()
            return redirect("/login")
       else:
           sg_form=signupform()
       contex={
           'form':sg_form
       }     
       return render(request,"signup.html",contex)
   

    
    
         
         
    
