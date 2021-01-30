from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='backend.login')
def index(request):
    contact = Contact.objects.all()[0]
    return render(request, 'contact/index.html', {'contact': contact})


@login_required(login_url='backend.login')
def edit(request, id):
    contact = Contact.objects.filter(id=id)[0]
    return render(request, 'contact/edit.html', {'contact': contact})


@login_required(login_url='backend.login')
def update(request, id):
    if request.method == 'POST':
        contact = Contact.objects.filter(id=id)
        contact.phone = request.POST['phone']
        contact.phone2 = request.POST['phone2']
        contact.email = request.POST['email']
        contact.address_uz = request.POST['address_uz']
        contact.address_ru = request.POST['address_ru']
        contact.telegram = request.POST['telegram']
        contact.instagram = request.POST['instagram']
        contact.twitter = request.POST['twitter']
        contact.facebook = request.POST['facebook']
        contact.save()
    return redirect('contact.index')

