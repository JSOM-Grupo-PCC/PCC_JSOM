from django.urls import path
from . import views

app_name = 'avaliacoes'

urlpatterns = [
    path('aluno/<int:aluno_id>/', views.lista_avaliacoes, name='lista_avaliacoes'),
    path('aluno/<int:aluno_id>/criar/', views.cria_avaliacao, name='cria_avaliacao'),
    path('<int:avaliacao_id>/atualizar/', views.atualiza_avaliacao, name='atualiza_avaliacao'),
    path('<int:avaliacao_id>/deletar/', views.deleta_avaliacao, name='deleta_avaliacao'),
]
