# Generated by Django 2.0.2 on 2018-12-03 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grades',
            old_name='gdirlnum',
            new_name='ggirlnum',
        ),
    ]