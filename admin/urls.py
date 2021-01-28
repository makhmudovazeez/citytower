from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='admin.index'),
    path('authorize/', views.authorize, name='admin.authorize'),

    # Users urls
    path('user/', views.user, name='admin.user'),
    path('user/create/', views.user_create, name='admin.user.create'),
    path('user/store/', views.user_store, name='admin.user.store'),
    path('user/edit/', views.user_edit, name='admin.user.edit'),
    path('user/update/', views.user_update, name='admin.user.update'),

    # Works urls
    path('works/create', views.works_create, name='admin.works.create'),
    path('works/store', views.works_store, name='admin.works.store'),
    path('works/edit', views.works_edit, name='admin.works.edit'),
    path('works/update', views.works_update, name='admin.works.update'),
    path('works/delete', views.works_delete, name='admin.works.delete'),

    # Contacts urls
    path('contact/', views.contact, name='admin.contact'),
    # path('contact/edit', views.contact_edit, name='admin.contact.edit'),
    # path('contact/update', views.contact_update, name='admin.contact.update'),

]
