from django.db import models


# Create your models here.

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
