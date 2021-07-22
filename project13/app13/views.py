from django.shortcuts import render

def showIndex(request):
    if request.method == "POST":
        username=request.POST.get("t1")
        password=request.POST.get("t2")
        type=request.POST.get("t3")


        if username == "Ravi":
            if password == "ravi1234@" and type == "admin":
                return render(request,"welcome.html",{"message":"admin"})
            elif password == "kumar@123" and type == "employee":
                return render(request,"welcome.html",{"message":"employee"})
            elif password == "ravikumar@123" and type == "customer":
                return render(request,"welcome.html",{"message":"customer"})
            else:
                return render(request,"index.html",{"data":"false"})
        else:
            return render(request,"index.html",{"data":"false"})


    elif request.method == "GET":
        return render(request,"index.html")

