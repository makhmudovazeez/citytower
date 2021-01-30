from django.db import models


# Create your models here.
class Services(models.Model):
    title_uz = models.CharField(max_length=200)
    title_ru = models.CharField(max_length=200)
    about_uz = models.TextField()
    about_ru = models.TextField()
    image = models.ImageField(upload_to='services')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
