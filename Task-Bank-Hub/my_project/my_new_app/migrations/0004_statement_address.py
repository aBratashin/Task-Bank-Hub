# Generated by Django 4.2.2 on 2023-11-09 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_new_app', '0003_delete_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='address',
            field=models.CharField(default=1, max_length=256, verbose_name='Адрес'),
            preserve_default=False,
        ),
    ]
