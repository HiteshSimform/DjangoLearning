from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def myfunction(request):
    return HttpResponse("Hello Django")

def learn_django(request,**kwargs):
    status = kwargs.get('status')
    return HttpResponse(f'<h1>Hello Django {status}</h1>')

def learn_python(request):
    return HttpResponse("<h1>Hello Python</h1>")

def learn_math(request):
    a = 10 + 10
    return HttpResponse(a)

def learn_php(request):
    lang = '<h1>Hello PHP</h1>'
    return HttpResponse(lang)

def myapp1(request):
    return HttpResponse('My App 1 Page')