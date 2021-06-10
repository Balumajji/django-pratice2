from django.shortcuts import render

def showIndex(request):
    if request.method == "POST":
        username=request.POST.get("t1")
        password=request.POST.get("t2")
        if username == "ravi" and password == "kumar":
            return render(request,"index.html", {"message":"valid"})
        else:
            return render(request,"index.html", {"message":"invalid"})

    if request.method == "GET":
        return render(request,"index.html")