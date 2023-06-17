from django.urls import path
from . import views
from chapters import urls

app_name = 'lectures'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:lecture_pk>/', views.detail, name='detail'),
    path('update/<int:lecture_pk>/', views.update, name='update'),
    path('delete/<int:lecture_pk>/', views.delete, name='delete'),
]