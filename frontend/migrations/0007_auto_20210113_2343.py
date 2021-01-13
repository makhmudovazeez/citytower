# Generated by Django 3.1.4 on 2021-01-13 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_auto_20210113_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sliders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_up_uz', models.CharField(max_length=30)),
                ('title_up_ru', models.CharField(max_length=30)),
                ('title_down_uz', models.CharField(max_length=30)),
                ('title_down_ru', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='about',
            name='open_close_ru',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='open_close_uz',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
