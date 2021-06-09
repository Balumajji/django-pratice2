from django.http import HttpResponse

def showindex(request):
    message =("Hello students welcome to Django calss")
    return HttpResponse(message)
