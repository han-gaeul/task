from django import forms
from .models import Chapter

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = [
            'title',
            'videofile',
        ]
        labels = {
            'title' : '제목',
            'videofile' : '동영상',
        }