from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='admin.index'),
    path('authorize/', views.authorize, name='authorize'),

    # Users urls
    path('user/', views.user, name='admin.user'),
    path('user/create/', views.user_create, name='admin.user.create'),
    path('user/store/', views.user_store, name='admin.user.store'),
    path('user/edit/', views.user_edit, name='admin.user.edit'),
    path('user/update/', views.user_update, name='admin.user.update'),
    path('user/delete/<int:id>', views.user_delete, name='admin.user.delete'),

    # Works urls
    path('works/', views.works, name='admin.works'),
    path('works/create', views.works_create, name='admin.works.create'),
    path('works/store', views.works_store, name='admin.works.store'),
    path('works/edit/<int:id>', views.works_edit, name='admin.works.edit'),
    path('works/update/<int:id>', views.works_update, name='admin.works.update'),
    path('works/delete/<int:id>', views.works_delete, name='admin.works.delete'),

    # Services urls
    path('services/', views.services, name='admin.services'),
    path('services/create', views.services_create, name='admin.services.create'),
    path('services/store', views.services_store, name='admin.services.store'),
    path('services/edit', views.services_edit, name='admin.services.edit'),
    path('services/update', views.services_update, name='admin.services.update'),
    path('services/delete', views.services_delete, name='admin.services.delete'),

    # Contacts urls
    path('contact/', views.contact, name='admin.contact'),
    # path('contact/edit', views.contact_edit, name='admin.contact.edit'),
    # path('contact/update', views.contact_update, name='admin.contact.update'),

    # About urls
    path('about/', views.about, name='admin.about'),
    path('about/create', views.about_create, name='admin.about.create'),
    path('about/store', views.about_store, name='admin.about.store'),
    path('about/edit', views.about_edit, name='admin.about.edit'),
    path('about/update', views.about_update, name='admin.about.update'),


]
