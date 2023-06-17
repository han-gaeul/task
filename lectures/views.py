from django.shortcuts import render, redirect, get_object_or_404
from .forms import LectureForm
from .models import Lecture

# Create your views here.

def index(request):
    lectures = Lecture.objects.all()
    content = {
        'lectures' : lectures
    }
    return render(request, 'lectures/index.html', content)

def create(request):
    if request.method == 'POST':
        form = LectureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lectures:index')
    else:
        form = LectureForm()
    context = {
        'form' : form,
    }
    return render(request, 'lectures/create.html', context)

def detail(request, lecture_pk):
    lecture = get_object_or_404(Lecture, pk=lecture_pk)
    chapters = lecture.chapters.all()
    context = {
        'lecture': lecture,
        'chapters' : chapters,
    }
    return render(request, 'lectures/detail.html', context)

def update(request, lecture_pk):
    lecture = get_object_or_404(Lecture, pk=lecture_pk)
    if request.method == 'POST':
        form = LectureForm(request.POST, instance=lecture)
        if form.is_valid():
            form.save()
            return redirect('lectures:detail', lecture_pk)
    else:
        form = LectureForm(instance=lecture)
    context = {
        'form' : form,
    }
    return render(request, 'lectures/update.html', context)

def delete(request, lecture_pk):
    lecture = get_object_or_404(Lecture, pk=lecture_pk)
    lecture.delete()
    return redirect('lectures:index')