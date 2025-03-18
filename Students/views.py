from tempfile import template
from django.shortcuts import render,redirect
from django.template import loader
from Students.models import Student
from django.http import HttpResponse 
from Students.forms import StudentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def students(request):
    students_list=Student.objects.all().values()
    template=loader.get_template('all_students.html')
    context={
        'students':students_list,
    } 
    return HttpResponse(template.render(context,request))


def details(request,id):
    st=Student.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
           'st_details':st
    }
    return HttpResponse(template.render(context,request))

def student_entry(request):
    if request.method=='POST':
     st_form=StudentForm(request.POST)
     if st_form.is_valid():
        st_form.save()
        return  redirect("success")
    else:
        st_form=StudentForm()
    template=loader.get_template('student_entry.html')
    context={
        'student_form':st_form
    }
    return HttpResponse(template.render(context,request))
def success(request):
   return render(request,'success.html')
    