from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("VOKA")
def detail(request,num):
    return HttpResponse("detail-%s"%num)

from .models import Grades,Students
from django.http import HttpResponse
def grades(request):
    #去模板里取数据
    gradesList = Grades.objects.all()
    # gradelist=[1,2,3]
    # print(gradesList)
    return render(request,'myApp/grades.html',{'grades':gradesList})
    pass

def students(request):
    #去模板里取数据
    studentsList = Students.objects.all()
    # gradelist=[1,2,3]
    # print(gradesList)
    return render(request,'myApp/students.html',{'students':studentsList})
    pass

def gradeStudents(request,num):
    #去模板里取数据
    grade = Grades.objects.get(pk=num)
    studentsList=grade.students_set.all()
    # gradelist=[1,2,3]
    # print(gradesList)
    return render(request,'myApp/students.html',{'students':studentsList})
    pass