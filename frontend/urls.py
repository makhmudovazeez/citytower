from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('project_details/', views.project_details, name='project_details'),
    path('service_details/', views.service_details, name='service_details'),
]