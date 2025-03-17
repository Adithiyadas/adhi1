from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from userAuthentication.forms import LoginForm


# Create your views here.
def getLoginPage(request):
    if(request.method=='GET'):

        form=LoginForm
        context={
            "form":form
        }

        return render(request,"login.html",context)

    elif(request.method=='POST'):
        loginForm=LoginForm(request.POST)

        if(loginForm.is_valid()):
            name=loginForm.cleaned_data["userName"]
            password=loginForm.cleaned_data["password"]

            user=authenticate(request,username=name,password=password)

            if user:
                login(request,user)
                return redirect("/students")

            messages.error(request,"invalid username or password!")
            context={
                "form":loginForm
            }

            return render(request,"login.html",context)

        


