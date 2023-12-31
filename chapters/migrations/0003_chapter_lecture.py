# Generated by Django 4.2.2 on 2023-06-17 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0006_remove_lecture_chapter'),
        ('chapters', '0002_remove_chapter_content_remove_chapter_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='lecture',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='lectures.lecture'),
            preserve_default=False,
        ),
    ]
