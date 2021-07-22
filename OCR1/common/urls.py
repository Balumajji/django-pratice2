from django.contrib import admin
from django.urls import path
from django.urls import include
from common import views


urlpatterns = [
    path(' ', views.showhome,name="home_page"),
]