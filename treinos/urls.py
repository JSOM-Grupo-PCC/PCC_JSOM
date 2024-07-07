# urls.py
from django.urls import path
from treinos import views

app_name = "treinos"

urlpatterns = [
    path('<int:aluno_id>/treino/', views.lista_treinos, name='lista_treinos'),
    path('<int:aluno_id>/treino/novo/', views.criar_treino, name='criar_treino'),
    path('<int:aluno_id>/treino/<int:pk>/editar/', views.editar_treino, name='editar_treino'),
    path('<int:aluno_id>/treino/<int:pk>/excluir/', views.excluir_treino, name='excluir_treino'),

    path('treinos/', views.meus_treinos, name='meus_treinos'),
    path('execucao_status/', views.execucao_status, name='execucao_status'),
]
