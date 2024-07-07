# urls.py
from django.urls import path
from . import views

app_name = "execucoes"

urlpatterns = [
    path('<int:treino_id>/execucoes/', views.lista_execucoes, name='lista_execucoes'),
    path('<int:treino_id>/execucao/nova/', views.criar_execucao, name='criar_execucao'),
    path('<int:treino_id>/execucao/<int:pk>/editar/', views.editar_execucao, name='editar_execucao'),
    path('<int:treino_id>/execucao/<int:pk>/excluir/', views.excluir_execucao, name='excluir_execucao'),
]
