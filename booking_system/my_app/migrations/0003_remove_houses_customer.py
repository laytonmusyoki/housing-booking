# Generated by Django 4.2.1 on 2023-06-23 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_houses_customer_alter_houses_image_delete_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houses',
            name='customer',
        ),
    ]
