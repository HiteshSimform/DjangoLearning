from django.shortcuts import render

# Create your views here.
def home(request):
    print("Home")
    return render(request,'myapp/home.html')

def about(request):
    print("About")
    return render(request,'myapp/about.html')