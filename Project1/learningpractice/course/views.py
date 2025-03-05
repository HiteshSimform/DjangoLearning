from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courses(req):
    return HttpResponse("<h1>Hello Courses</h1>")