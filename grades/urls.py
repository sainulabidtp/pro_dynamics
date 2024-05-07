from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/', views.student_create, name='student_create'),
    path('update/<int:pk>/', views.student_update, name='student_update'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('search/', views.student_search, name='student_search'),
    path('subject/', views.subject_list, name='subject_list'),
    path('subject/create/', views.subject_create, name='subject_create'),
    path('subject/update/<int:pk>/', views.subject_update, name='subject_update'),
    path('subject/delete/<int:pk>/', views.subject_delete, name='subject_delete'),
]
