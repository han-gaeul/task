# Generated by Django 4.2.2 on 2023-06-15 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0001_initial'),
        ('lectures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='chapter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='chapters.chapter'),
        ),
    ]
