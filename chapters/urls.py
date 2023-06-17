from django.urls import path
from . import views

app_name = 'chapters'

urlpatterns = [
    path('create/<int:lecture_pk>/', views.create, name='create'),
    path('update/<int:lecture_pk>/<int:chapter_pk>/', views.update, name='update'),
    path('delete/<int:lecture_pk>/<int:chapter_pk>/', views.delete, name='delete'),
]