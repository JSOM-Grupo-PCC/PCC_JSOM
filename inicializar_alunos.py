import os
import django
from faker import Faker

# Configurar o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_jsom.settings')
django.setup()

from django.contrib.auth.models import Group
from usuarios.models import Usuario

def inicializar_dados():
    # Criar ou obter o grupo "Aluno"
    grupo_aluno, created = Group.objects.get_or_create(name='Aluno')
    
    # Configurar o Faker para gerar dados fictícios
    fake = Faker('pt_BR')
    
    # Número de usuários a serem criados
    num_usuarios = 50
    
    for _ in range(num_usuarios):
        username = fake.user_name()
        password = fake.password()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=65)
        cpf = fake.cpf()
        endereco = fake.address()
        
        # Criar o usuário
        usuario = Usuario.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            data_nascimento=data_nascimento,
            cpf=cpf,
            endereco=endereco
        )
        
        # Adicionar o usuário ao grupo "Aluno"
        usuario.groups.add(grupo_aluno)
        usuario.save()

    print(f"{num_usuarios} usuários criados e adicionados ao grupo 'Aluno' com sucesso.")

if __name__ == '__main__':
    inicializar_dados()
