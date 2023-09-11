# Generated by Django 4.2.5 on 2023-09-11 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_remove_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
