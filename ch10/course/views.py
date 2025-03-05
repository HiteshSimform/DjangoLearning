from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def learn_django(req):
#     return HttpResponse('<h1>Hello Django from Course App</h1>')

def learn_django(req):
    return render(req,'course/django.html')

def learn_fastapi(req):
    return render(req,'course/fastapi.html')