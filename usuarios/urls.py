from django.urls import path
from . import views

app_name = "usuario"

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.lista_alunos, name='lista_alunos'),
    path('aluno/<int:aluno_id>/', views.aluno_perfil, name='aluno_perfil'),
    path('aluno/updade/<int:aluno_id>/', views.aluno_updade, name='aluno_updade'),
]
