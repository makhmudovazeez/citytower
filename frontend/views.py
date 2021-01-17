from django.shortcuts import render
from .models import Contacts
from django.http import HttpResponse


def session(request):
    my_contact = Contacts
    try:
        my_contact = Contacts.objects.get()
    except my_contact.DoesNotExist:
        my_contact.phone = "+998909696293"
        my_contact.phone2 = "+998909696293"
        my_contact.email = "constructiontowersm@gmail.com"
        my_contact.address_ru = "Боткина"
        my_contact.address_uz = "Botkina"
    request.session.my_contact = my_contact


def index(request):
    session(request)
    # return HttpResponse(request.session.my_contact.email)
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
