from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World")

@csrf_exempt
def my_view(request):
    if request.method == 'GET':
        return HttpResponse("This is a GET request")
    elif request.method == 'POST':
        return HttpResponse("This is a POST request")
    else:
        return HttpResponse("Unsupported request method", status=405)
