from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='contact.index'),
    path('edit/<int:id>', views.edit, name='contact.edit'),
    path('update/<int:id>', views.update, name='contact.update')
]
