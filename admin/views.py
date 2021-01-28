from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Contacts


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
    users = User.objects.all()
    return render(request, 'admin/users/index.html', {'users': users})


def user_create(request):
    return render(request, 'admin/users/create.html')


def user_store(request):
    pass


def user_edit(request):
    pass


def user_update(request):
    pass


# Works Actions
def works(request):
    return render(request, 'admin/works/index.html')


def works_create(request):
    pass


def works_store(request):
    pass


def works_edit(request):
    pass


def works_update(request):
    pass


def works_delete(request):
    pass


def contact(request):
    my_contact = Contacts.objects.get(pk=1)
    return render(request, 'admin/contacts/index.html', {'contact': my_contact})
