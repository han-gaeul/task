# Generated by Django 4.2.2 on 2023-06-17 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='content',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='chapter',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
    ]