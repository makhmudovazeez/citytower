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
