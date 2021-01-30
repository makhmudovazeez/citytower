from django.shortcuts import render
from contact.models import Contact
from works.models import Works
from services.models import Services
from django.http import HttpResponse


def session(request):
    try:
        my_contact = Contact.objects.get(pk=1)
    except:
        Contact.objects.create_contact('constructiontowersm@gmail.com', '+998998609464', '+998977467878')
        my_contact = Contact.objects.get(pk=1)
    request.session.my_contact = my_contact


def index(request):
    session(request)
    # return HttpResponse(request.LANGUAGE_CODE)
    services = Services.objects.all()
    works = Works.objects.all()
    return render(request, 'frontend/index.html', {'services': services, 'works': works})


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
