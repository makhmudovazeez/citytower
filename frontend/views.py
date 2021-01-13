from django.shortcuts import render


def index(request):
    return render(request, 'frontend/index.html')


def about(request):
    return render(request, 'frontend/about.html')


def projects(request):
    return render(request, 'frontend/projects.html')


def contact(request):
    return render(request, 'frontend/contact.html')


def project_details(request):
    return render(request, 'frontend/project_details.html')


def service_details(request):
    return render(request, 'frontend/service_details.html')
