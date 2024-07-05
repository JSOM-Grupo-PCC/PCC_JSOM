# urls.py
from django.urls import path
from . import views

app_name = "exercicios"

urlpatterns = [
    path('grupos/', views.grupo_muscular_list, name='grupo_muscular_list'),
    path('grupos/add/', views.grupo_muscular_create, name='grupo_muscular_create'),
    path('grupos/<int:pk>/edit/', views.grupo_muscular_update, name='grupo_muscular_update'),
    path('grupos/<int:pk>/delete/', views.grupo_muscular_delete, name='grupo_muscular_delete'),
]
