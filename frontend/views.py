from django.shortcuts import render
from .models import Contacts
from django.utils.translation import gettext as _
from django.http import HttpResponse


def session(request):
    contact = Contacts.objects.get()
    request.session.contact = contact


def index(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)
    session(request)
    return render(request, 'frontend/index.html')


def about(request):
    session(request)
    return render(request, 'frontend/about.html')


def projects(request):
    session(request)
    return render(request, 'frontend/projects.html')


def contact(request):
    session(request)
    return render(request, 'frontend/contact.html')


def project_details(request):
    session(request)
    return render(request, 'frontend/project_details.html')


def service_details(request):
    session(request)
    return render(request, 'frontend/service_details.html')
