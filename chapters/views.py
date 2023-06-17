from django.shortcuts import render, redirect, get_object_or_404
from lectures.models import Lecture
from .models import Chapter
from .forms import ChapterForm

# Create your views here.

def create(request, lecture_pk):
    lecture = Lecture.objects.get(id=lecture_pk)
    if request.method == 'POST':
        form = ChapterForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.lecture = lecture
            form.save()
            return redirect('lectures:detail', lecture_pk=form.lecture.id)
    else:
        form = ChapterForm()
    context = {
        'form' : form,
    }
    return render(request, 'chapters/create.html', context)

def update(request, lecture_pk, chapter_pk):
    lecture = Lecture.objects.get(id=lecture_pk)
    chapter = Chapter.objects.get(id=chapter_pk)
    if request.method == 'POST':
        form = ChapterForm(request.POST, request.FILES, instance=chapter)
        if form.is_valid():
            form = form.save(commit=False)
            form.lecture = lecture
            form.save()
            return redirect('lectures:detail', lecture_pk=form.lecture.id)
    else:
        form = ChapterForm(instance=chapter)
    context = {
        'form' : form,
    }
    return render(request, 'chapters/update.html', context)

def delete(request, chapter_pk, lecture_pk):
    chapter = get_object_or_404(Chapter, pk=chapter_pk)
    chapter.delete()
    return redirect('lectures:detail', lecture_pk=lecture_pk)