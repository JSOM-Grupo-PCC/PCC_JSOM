# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:aluno_id>/treino/', views.programa_list, name='programa_list'),
    path('<int:aluno_id>/treino/new/', views.programa_create, name='programa_create'),
    path('<int:aluno_id>/treino/<int:pk>/edit/', views.programa_update, name='programa_update'),
    path('<int:aluno_id>/treino/<int:pk>/delete/', views.programa_delete, name='programa_delete'),
]
