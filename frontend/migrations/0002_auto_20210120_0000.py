# Generated by Django 3.1.4 on 2021-01-19 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(upload_to='services'),
        ),
        migrations.AlterField(
            model_name='woksimages',
            name='image',
            field=models.ImageField(upload_to='works'),
        ),
    ]