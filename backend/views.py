from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    return render(request, 'backend/login.html')


def authorize(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        staff = auth.authenticate(username=username, password=password)

        if staff is not None:
            auth.login(request, staff)
            return redirect('backend.index')
        else:
            return redirect('login')
    return redirect('login')


@login_required(login_url='backend.login')
def index(request):
    return render(request, 'backend/index.html')
