from datetime import datetime
from django.db import models


# Create your models here.

class Works(models.Model):
    title_uz = models.CharField(max_length=225)
    title_ru = models.CharField(max_length=225)
    description_uz = models.TextField()
    description_ru = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)


class WoksImages(models.Model):
    image = models.ImageField(upload_to='works')
    work_id = models.ForeignKey(
        Works,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class Orders(models.Model):
    STATUS = (
        ('Pending', 'В ожидании'),
        ('Canceled', 'Отменено'),
        ('Received', 'Принято')
    )
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    address = models.TextField()
    message = models.TextField()
    status = models.CharField(max_length=50, default=STATUS[0][0], choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class About(models.Model):
    about_uz = models.TextField()
    about_ru = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class ContactsManager(models.Manager):
    def create_contact(self, email, phone, phone2):
        main_contact = self.create(email=email, phone=phone, phone2=phone2)
        return main_contact


class Contacts(models.Model):
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=13)
    phone2 = models.CharField(max_length=13, null=True, blank=True)
    address_uz = models.TextField(max_length=255, null=True, blank=True)
    address_ru = models.TextField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    objects = ContactsManager()


class Services(models.Model):
    title_uz = models.CharField(max_length=200)
    title_ru = models.CharField(max_length=200)
    about_uz = models.TextField()
    about_ru = models.TextField()
    image = models.ImageField(upload_to='services')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
