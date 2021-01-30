from django.db import models


# Create your models here.
class About(models.Model):
    about_uz = models.TextField()
    about_ru = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
