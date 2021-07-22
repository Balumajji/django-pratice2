from django.shortcuts import render,redirect
from app18.models import studentregistration

def showIndex(request):
    return render(request,"index.html")

def showadmin(request):
    return render(request,'admin.html',{"student_info":studentregistration.objects.all()})

def showstudentdata(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact= request.POST.get("contact")
        email = request.POST.get("email")
        password = request.POST.get("password")
        photo = request.FILES['photo']
        dob = request.POST.get("dob")

        studentregistration(name=name,contact=contact,email=email,password=password,dob=dob,photo=photo).save()
        return redirect('main')

def showdeletestudent(request,student_number):
    student_data= studentregistration.objects.get(number=student_number)
    if request.method == "POST":
        student_data.delete()
        return render(request,"admin.html",{"student_info":studentregistration.objects.all()})
    else:
        return render(request,"delete_student.html",{"student_info":student_data})


