from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import CustomUser
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data("password")
            user.save()
            messages.success(request,"Registered Successfully")
            return redirect("login")
    else:
        form=RegisterForm()
    return render(request,'accounts/register.html')