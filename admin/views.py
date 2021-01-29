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


def services(request):
    return render(request, 'admin/services/index.html')


def services_create(request):
    return render(request, 'admin/services/create.html')


def services_store(request):
    pass


def services_edit(request):
    return render(request, 'admin/services/edit.html')


def services_update(request):
    pass


def services_delete(request):
    pass


def about(request):
    return render(request, 'admin/about/index.html')


def about_create(request):
    return render(request, 'admin/about/create.html')


def about_store(request):
    pass


def about_edit(request):
    return render(request, 'admin/about/edit.html')


def about_update(request):
    pass


def contact(request):
    my_contact = Contacts.objects.get(pk=1)
    return render(request, 'admin/contacts/index.html', {'contact': my_contact})
