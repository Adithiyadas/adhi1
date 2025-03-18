from django import forms
from Students.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['firstName','lastName','age','email']