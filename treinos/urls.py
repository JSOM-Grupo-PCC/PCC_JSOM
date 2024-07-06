# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:treino_id>/execucao/', views.treino_list, name='treino_list'),
    path('<int:treino_id>/execucao/new/', views.treino_create, name='treino_create'),
    path('<int:treino_id>/execucao/<int:pk>/edit/', views.treino_update, name='treino_update'),
    path('<int:treino_id>/execucao/<int:pk>/delete/', views.treino_delete, name='treino_delete'),
]
