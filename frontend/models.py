from datetime import datetime
from django.db import models


# Create your models here.

class Works(models.Model):
    title_uz = models.CharField(max_length=225)
    title_ru = models.CharField(max_length=225)
    description_uz = models.TextField()
    description_ru = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.name


class WoksImages(models.Model):
    image = models.ImageField(upload_to='works')
    work_id = models.ForeignKey(
        Works,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    address = models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.name


class About(models.Model):
    about_uz = models.TextField()
    about_ru = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=13)
    phone2 = models.CharField(max_length=13, null=True)
    address_uz = models.TextField()
    address_ru = models.TextField()
    open_close_uz = models.TextField(max_length=255, null=False)
    open_close_ru = models.TextField(max_length=255, null=False)
    telegram = models.CharField(max_length=100, null=True, blank=False)
    instagram = models.CharField(max_length=100, null=True, blank=False)
    twitter = models.CharField(max_length=100, null=True, blank=False)
    facebook = models.CharField(max_length=100, null=True, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.name


class Services(models.Model):
    title_uz = models.CharField(max_length=200)
    title_ru = models.CharField(max_length=200)
    about_uz = models.TextField()
    about_ru = models.TextField()
    image = models.ImageField(upload_to='services')
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.name
