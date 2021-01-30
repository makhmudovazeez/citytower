from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='services.index'),
    path('create/', views.create, name='services.craete'),
    path('store/', views.store, name='services.store'),
    path('edit/<int:id>', views.edit, name='services.edit'),
    path('update/<int:id>', views.update, name='services.update'),
    path('delete/<int:id>', views.delete, name='services.delete'),
]
