from django.shortcuts import render,redirect
from app20.models import courseModel,studentModel
from app20.forms import courseForm,studentForm

def showIndex(request):
    course = courseForm(request.POST)
    if request.method == "POST":
        course.save()
        return render(request,"index.html",{"c_form":courseForm(),"message":"Course was added"})
    else:
        return render(request,"index.html",{"c_form":courseForm(),"all_courses":courseModel.objects.all()})

def showStudent(request):
    student = studentForm(request.POST)
    if request.method == "POST":
        student.save()
        return render(request, "student.html", {"s_form": studentForm(), "message": "student was added"})
    else:
        result = courseModel.objects.all()
        if result:
            return render(request,"student.html",{"s_form":studentForm(),"all_students":studentModel.objects.all()})
        else:
            return render(request,"student.html",{"error":"please add the course"})

