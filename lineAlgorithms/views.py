from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import AdditionForm

# Create your views here.

def home(request):
    result = None
    
    if request.method == 'POST':
        form = AdditionForm(request.POST)
        if form.is_valid():
            number1 = form.cleaned_data['number1']
            number2 = form.cleaned_data['number2']
            result = number1 + number2

    else:
        form = AdditionForm()

    return render(request, 'home.html',{'form':form, 'result':result})


def brensenham(request):
    return render(request, template_name="brensenham.html")

def DDA(request):
    return render(request, template_name="DDA.html")
