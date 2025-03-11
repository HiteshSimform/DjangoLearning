from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.http import HttpResponse
# Create your views here.

# contact/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

# View All Contact Submissions
def view_all_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contact/view_all_contacts.html', {'contacts': contacts})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
        else:
            form = ContactForm()
    return render(request, 'contact/contact_form.html',{'form':form})

def thank_you_view(request):
    return render(request, 'contact/thank_you.html')

def show_all(request):
    contacts = Contact.objects.filter(name='b')
    return render(request,'contact/details.html',{'items':contacts})
# Detete form details

from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return HttpResponse("Welcome to your profile")

# contact/views.py

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('view_all_contacts')  # Redirect to the page that shows all submissions
    return render(request, 'contact/confirm_delete.html', {'contact': contact})

# contact/views.py

def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('view_all_contacts')  # Redirect to the page that shows all submissions
    else:
        form = ContactForm(instance=contact)
    
    return render(request, 'contact/contact_form.html', {'form': form})
