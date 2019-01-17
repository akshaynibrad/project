from django.http import HttpResponse
from django.shortcuts import *
from django.shortcuts import render

def one(request):
    return render(request,'one.html')

def two(request):
    return render(request,'two.html')