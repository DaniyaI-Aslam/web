# Generated by Django 3.2.8 on 2021-12-13 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20211213_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='recommended_by10',
        ),
    ]
