from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import FileUpload
import time

# Create your views here.

def convert(request):
    if request.method == 'POST':
        img = request.FILES["imgfile"]
        fileupload = FileUpload(
            imgfile=img,
        )
        fileupload.save()
        #time.sleep(10)
        return render(request, "DeePepper/convert.html", {
            "fileupload": fileupload,
        })
    else:
        return render(request, 'DeePepper/convert.html')

def home(request):
    fileuploadForm = FileUploadForm
    context = {
        'fileuploadForm': fileuploadForm,
    }
    return render(request, 'DeePepper/home.html', context)