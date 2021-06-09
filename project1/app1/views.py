from django.shortcuts import render
from django.http import HttpResponse

def wish(request):
    message = "Welcome to django"
    return HttpResponse(message)
