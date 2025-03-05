from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

# def learn_django(req):
#     return HttpResponse('<h1>Hello Django from Course App</h1>')


# def learn_django(req):
#     coursename = {"cname": "Django 5.1"}
#     return render(req, "course/django.html", context=coursename)


# def learn_django(req):
#     return render(req,'course/django.html',{'name':'Django'})

# def learn_django(req):
#     coursename = {'cname':'Django 5.1'}
#     return render(req,'course/django.html',coursename)


# Example - 1.2 - Variable
# def learn_django(req):
#     name = 'Django'
#     duration = '4 months'
#     seats = 10
#     coursedetail = {'nm':name,'du':duration,'st':seats}
#     return render(req, "course/django.html", coursedetail)

def learn_fastapi(req):
    seats = 10
    coursedetail = {"cname": "FAST API", "version": "3.0", "st": seats}
    return render(req, "course/fastapi.html", coursedetail)


# Example 2 - Filter

# def learn_django(req):
#     return render(req, "course/django.html", context={"name": "Django",'desc':'Django is awesome web framework'})

# Example 3 - Date and Time


def learn_django(req):
    d=datetime.now()
    return render(req, "course/django.html", context={"dt":d})