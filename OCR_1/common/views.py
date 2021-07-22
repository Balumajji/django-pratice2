from django.shortcuts import render
from student.models import StudentRegistration
from django.db.models import Q
from random import randint
from common.utils import sendTextMessage
from django.shortcuts import redirect

def showHome(request):
    return render(request,"common/home.html")

def showstudent(request):
    return render(request,"common/student.html")

def showStudentRegistration(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        password = request.POST.get("password")

        record =  StudentRegistration.objects.filter(Q(contact=contact) | Q(email=email))
        if record:
            return render(request,'common/student.html', {"data":[name,contact,email,'Email or Contact Number is already available']})
        else:
            otp = randint(10000,99999)
            message = ''' Thank you for registered with sathya tech., to complete your registration use the given otp.
            Your OTP: '''+str(otp)
            if sendTextMessage(message,contact):
                StudentRegistration(name=name,contact=contact,email=email,password=password).save()
                return redirect('student_otp')
            else:
                return render(request, 'common/student.html', {"data": [name, contact, email, 'Wrong contact number']})


    else:
        showstudent(request)

def showstudentotp(request):
    return render(request,"common/otp.html")

def showfaculty(request):
    return render(request,"common/faculty.html")

def showadmin(request):
    return render(request,"common/admin_OCR.html")

def showcontact(request):
    return render(request,"common/contact.html")


