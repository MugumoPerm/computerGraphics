from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, template_name="home.html")


def brensenham(request):
    return render(request, template_name="brensenham.html")

def DDA(request):
    return render(request, template_name="DDA.html")
