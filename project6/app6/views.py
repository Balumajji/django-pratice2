from django.shortcuts import render

def showIndex(request):
    emp_info= {"idno":101,"Name":"santosh","salary":220000.00}
    return render(request,"main.html",emp_info)
