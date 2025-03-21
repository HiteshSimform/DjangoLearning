from django.shortcuts import render, redirect
from .forms import RegisterUser
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import CustomUser

from .utils import role_required
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("form saved")
    form = RegisterUser
    return render(request, 'accounts/upload.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("request test")
        if form.is_valid():
            # user = form.save()
            form.save()
            # print("request test form valid")
            # username = request.POST['username']
            # password = request.POST['password']
            # user = authenticate(request,username=username,password=password)
            # login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

@role_required('admin')
def admin_view(request):
    return render(request,'accounts/admin_dashboard.html')


@login_required
def home(request):
    return render(request,'accounts/home.html')

