# Generated by Django 4.2.2 on 2023-06-15 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0002_alter_lecture_chapter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='chapter',
        ),
    ]