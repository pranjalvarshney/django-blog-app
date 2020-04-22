from django.shortcuts import render

# Create your views here.
def articles(res):
    return render(res,'articles.html')