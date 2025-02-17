# from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    # return HttpResponse("hola i am home page!")
    return render(request,'homePage.html')

def aboutPage(request):
    # return HttpResponse("hola i am about page!")
    return render(request,'aboutPage.html')