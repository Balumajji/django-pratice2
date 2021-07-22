from django.shortcuts import render

def showIndex(request):
    return render(request,"main.html")

def showregister(request):
    return render(request,"register.html")

def showlogin(request):
    return render(request,"login.html")
