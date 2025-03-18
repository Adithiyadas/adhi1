from django.shortcuts import render,redirect
from django.template import loader
from Students.models import Student
from Students.forms import StudentForm
from django.contrib.auth.decorators import login_required


from django.http import HttpResponse

@login_required
def getStudents(request):
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

def getStudentForm(request):
    if request.method=='POST':
        student_form=StudentForm(request.POST)

        if student_form.is_valid():
            student_form.save()
            return redirect("success")
        
    else:
        student_form=StudentForm()

    template=loader.get_template('studentEntry.html')
    context={
        'student_form':student_form
    }

    return HttpResponse(template.render(context,request))

def success(request):
    print('hello!')
    return render(request,'success.html')

def details(request,id):
    student=Student.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'student_detail':student
    }

    return HttpResponse(template.render(context,request))



