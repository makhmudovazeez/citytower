from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from about.models import About
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='backend.login')
def index(request):
    try:
        about = About.objects.get(pk=1)
    except:
        return redirect('about.create')
    return render(request, 'about/index.html', {'about': about})


@login_required(login_url='backend.login')
def create(request):
    try:
        about = About.objects.get(pk=1)
        if about is not None:
            return redirect('about.index')
        else:
            return render(request, 'about/create.html')
    except:
        return render(request, 'about/create.html')


@login_required(login_url='backend.login')
def store(request):
    if request.method == 'POST':
        about_ru = request.POST['about_ru']
        about_uz = request.POST['about_uz']
        about = About(about_ru=about_ru, about_uz=about_uz)
        about.save()
        return redirect('about.index')
    return redirect('about.create')


@login_required(login_url='backend.login')
def edit(request, id):
    about = About.objects.filter(id=id)[0]
    if about is not None:
        return render(request, 'about/edit.html', {'about': about})
    return redirect('about.index')


@login_required(login_url='backend.login')
def update(request, id):
    if request.method == 'POST':
        about = About.objects.filter(id=id)[0]
        about_uz = request.POST['about_uz']
        about_ru = request.POST['about_ru']
        about.about_ru = about_ru
        about.about_uz = about_uz
        about.save()
        return redirect('about.index')
    return redirect('about.edit')

