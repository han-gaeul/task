from django import forms
from .models import Lecture

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = [
            'title',
            'content',
        ]
        labels = {
            'title' : '제목',
            'content' : '설명',
        }