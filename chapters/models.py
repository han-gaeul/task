from django.db import models
from lectures.models import Lecture

# Create your models here.

class Chapter(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=100)
    videofile = models.FileField(upload_to='videos/', null=True)