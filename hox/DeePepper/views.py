from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'DeePepper/home.html')

def convert(request):
    return render(request, 'DeePepper/convert.html')