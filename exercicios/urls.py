# urls.py
from django.urls import path
from exercicios import views

app_name = "exercicios"

urlpatterns = [
    # Grupo Muscular
    path('grupos/', views.grupo_muscular_list, name='grupo_muscular_list'),
    path('grupos/criar/', views.grupo_muscular_create, name='grupo_muscular_create'),
    path('grupos/<int:pk>/editar/', views.grupo_muscular_update, name='grupo_muscular_update'),
    path('<int:pk>/deletar/', views.grupo_muscular_delete, name='grupo_muscular_delete'),
    # path('grupos/<int:pk>/excluir/', views.grupo_muscular_delete, name='grupo_muscular_delete'),

    # Exercicios
    path('', views.exercicio_list, name='exercicio_list'),
    path('criar/', views.exercicio_create, name='exercicio_create'),
    path('<int:pk>/editar/', views.exercicio_update, name='exercicio_update'),
    path('<int:pk>/excluir/', views.exercicio_delete, name='exercicio_delete'),
]
