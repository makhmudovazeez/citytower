from django.shortcuts import render, redirect
from .models import Services
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='backend.login')
def index(request):
    return render(request, 'services/index.html')


@login_required(login_url='backend.login')
def create(request):
    return render(request, 'server/create.html')


@login_required(login_url='backend.login')
def store(request):
    if request.method == 'POST':
        service = Services(
            title_ru=request.POST['title_ru'], title_uz=request.POST['title_uz'],
            about_ru=request.POST['about_ru'], about_uz=request.POST['about_uz'],
            image=request.POST['image'])
        service.save()
    else:
        return redirect('services.create')
    return redirect('services.index')

@login_required(login_url='backend.login')
def edit(request, id):
    service = Services.objects.filter(id=id)
    return render(request, 'services/edit.html', {'service': service})


@login_required(login_url='backend.login')
def update(request, id):
    if request.method == 'POST':
        service = Services.objects.filter(id=id)
        service.title_ru = request.POST['title_ru']
        service.title_uz = request.POST['title_uz']
        service.about_ru = request.POST['about_ru']
        service.about_uz = request.POST['about_uz']
        service.image = request.image['image']
        service.save()
    else:
        return redirect('services.create')
    return redirect('services.index')


@login_required(login_url='backend.login')
def delete(request, id):
    Services.objects.filter(id=id).delete()
    return redirect('services.index')