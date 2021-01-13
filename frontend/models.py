from datetime import datetime
from django.db import models


# Create your models here.


class Works(models.Model):
    title_uz = models.CharField(max_length=225)
    title_ru = models.CharField(max_length=225)
    description_uz = models.TextField()
    description_ru = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)


class WoksImages(models.Model):
    image = models.ImageField(upload_to='upload')
    work_id = models.ForeignKey(
        Works,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)


class Feedback(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    address = models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)


class About(models.Model):
    about_uz = models.TextField()
    about_ru = models.TextField()
    open_close_uz = models.TextField(max_length=255, blank=True, null=True)
    open_close_ru = models.TextField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)


class Contacts(models.Model):
    phone = models.CharField(max_length=13)
    phone2 = models.CharField(max_length=13, null=True)
    address_uz = models.TextField()
    address_ru = models.TextField()
    email = models.CharField(max_length=100, null=True)
    telegram = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)


class Services(models.Model):
    title_uz = models.CharField(max_length=200)
    title_ru = models.CharField(max_length=200)
    about_uz = models.TextField()
    about_ru = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

# class Position(models.Model):
#     title_uz = models.CharField(max_length=50)
#     title_ru = models.CharField(max_length=50)
#     created_at = models.DateTimeField(default=datetime.now, blank=True)
#     updated_at = models.DateTimeField(default=datetime.now, blank=True)


# class Employee(models.Model):
#     full_name = models.CharField(max_length=100)
#     position_id = models.ForeignKey(
#         Position,
#         on_delete=models.CASCADE,
#         blank=True,
#         null=True
#     )
#     created_at = models.DateTimeField(default=datetime.now, blank=True)
#     updated_at = models.DateTimeField(default=datetime.now, blank=True)


# class Sliders(models.Model):
#     title_center_up_uz = models.CharField(max_length=30)
#     title_center_up_ru = models.CharField(max_length=30)
#     title_center_down_uz = models.CharField(max_length=30)
#     title_center_down_ru = models.CharField(max_length=30)
#     image = models.ImageField()
#     status = models.BooleanField(default=1)
#     created_at = models.DateTimeField(default=datetime.now, blank=True)
#     updated_at = models.DateTimeField(default=datetime.now, blank=True)
