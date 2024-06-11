from django.urls import path
from . import views

app_name = "usuario"

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),  # Certifique-se de criar uma view `index`
]
