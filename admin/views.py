from django.shortcuts import render
from django.http import HttpResponse
from auth.models import Users


# Create your views here.

# Auth actions
def login(request):
    return render(request, 'admin/login.html')


def authorize(request):
    return HttpResponse('auth')


# Crud actions
def index(request):
    return render(request, 'admin/index.html')


# User actions
def user(request):
    users = Users.objects.all()
    return HttpResponse(users)
    return render(request, 'admin/users/index.html', {'users':users})


def user_create(request):
    return render(request, 'admin/users/create.html')
