from django.db import models


# Create your models here.
class ContactManager(models.Manager):
    def create_contact(self, email, phone, phone2):
        main_contact = self.create(email=email, phone=phone, phone2=phone2)
        return main_contact


class Contact(models.Model):
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
    objects = ContactManager()
