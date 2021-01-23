from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='admin.index'),
    path('authorize/', views.authorize, name='admin.authorize'),
    path('user/', views.user, name='admin.user'),
    path('user/create/', views.user_create, name='admin.user.create')
]
