from django.urls import path
from . import views

urlpatterns=[
    path('',views.getLoginPage,name='login'),
    path('signUp/',views.getSignUpPage,name='signup')
]