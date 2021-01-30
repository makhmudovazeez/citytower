from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index, name='backend.index'),
    path('login/', views.login, name='backend.login'),
    path('authorize/', views.authorize, name='backend.authorize'),
]
