from django.urls import path
from . import views 
urlpatterns = [
    path('',views.getStudents),
    path('entry/',views.getStudentForm,name='entry'),
    path('success/',views.success,name='success'),
    path('details/<int:id>',views.details,name='details')
]
