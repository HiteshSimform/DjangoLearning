from django.shortcuts import render
from .forms import FileUploadForm

# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'uploader/success.html')
    else:
        form = FileUploadForm()
    return render(request,'uploader/upload.html',{'form':form})