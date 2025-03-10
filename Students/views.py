from django.shortcuts import render
from django.template import loader
from Students.models import Student
from Students.forms import StudentForm

from django.http import HttpResponse

def getStudents(request):
    students_list=Student.objects.all().values()
    template=loader.get_template('studentsPage.html')

    context={
        'students':students_list
    }

    return HttpResponse(template.render(context,request))

def getStudentForm(request):
    student_form=StudentForm
    template=loader.get_template('studentEntry.html')
    context={
        'student_form':student_form
    }

    return HttpResponse(template.render(context,request))