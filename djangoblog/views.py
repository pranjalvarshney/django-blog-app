from django.http import HttpResponse
from django.shortcuts import render

def home(res):
    # return HttpResponse('home')
    return render(res,'index.html')

def about(res):
    # return HttpResponse('about')
    return render(res,'about.html')
