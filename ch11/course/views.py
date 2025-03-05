from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def learn_django(req):
#     return HttpResponse('<h1>Hello Django from Course App</h1>')


def learn_django(req):
    coursename = {"cname": "Django 5.1"}
    return render(req, "course/django.html", context=coursename)


# def learn_django(req):
#     return render(req,'course/django.html',{'cname':'Django 5.1'})

# def learn_django(req):
#     coursename = {'cname':'Django 5.1'}
#     return render(req,'course/django.html',coursename)


def learn_fastapi(req):
    seats = 10
    coursedetail = {"cname": "FAST API", "version": "3.0", "st": seats}
    return render(req, "course/fastapi.html", coursedetail)
