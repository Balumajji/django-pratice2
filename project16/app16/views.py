from django.shortcuts import render
from app16.models import Registration

def showIndex(request):
    return render(request,"main.html")

def showRegister(request):
    if request.method == "POST":
        n = request.POST.get("name")
        cont = request.POST.get("contact")
        loc = request.POST.get("location")
        email = request.POST.get("email")
        password = request.POST.get("password")

        Registration(name=n,contact=cont,location=loc,email=email,password=password).save()

        return render(request,"register.html", {"message":"Registration is done"})
    else:
        return render(request,"register.html")

def showLogin(request):
    return render(request,"login.html")