from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'frontend/index.html')

def about(request):
    return render(request, 'frontend/about.html')

def projects(request):
    return render(request, 'frontend/projects.html')

def contact(request):
    return render(request, 'frontend/contact.html')