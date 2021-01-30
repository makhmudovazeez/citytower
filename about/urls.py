from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='about.index'),
    path('create/', views.create, name='about.create'),
    path('store/', views.store, name='about.store'),
    path('edit/<int:id>', views.edit, name='about.edit'),
    path('update/<int:id>', views.update, name='about.update'),
]
