# Generated by Django 3.1.4 on 2021-01-13 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_about_contacts_employee_feedback_images_position_works'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='position_id',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.RemoveField(
            model_name='images',
            name='work_id',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
        migrations.DeleteModel(
            name='Works',
        ),
    ]
