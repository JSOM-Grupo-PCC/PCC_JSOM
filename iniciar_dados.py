import os
import django
from faker import Faker

# Configurar o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_jsom.settings')
django.setup()

from django.contrib.auth.models import Group
from usuarios.models import Usuario
from exercicios.models import GrupoMuscular, Exercicio

def inicializar_dados():
    # Criar ou obter o grupo "Aluno"
    grupo_aluno, created = Group.objects.get_or_create(name='Aluno')
    
    # Criar ou obter o grupo "Personal"
    grupo_personal, created = Group.objects.get_or_create(name='Personal')
    
    # Configurar o Faker para gerar dados fictícios
    fake = Faker('pt_BR')
    
    # Número de usuários a serem criados para o grupo "Aluno"
    num_usuarios = 50
    senha_padrao = 'aluno1234'
    
    for _ in range(num_usuarios):
        username = fake.user_name()
        
        # Verificar se o usuário já existe
        if not Usuario.objects.filter(username=username).exists():
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=65)
            cpf = fake.cpf()
            endereco = fake.address()
            
            # Criar o usuário
            usuario = Usuario.objects.create_user(
                username=username,
                password=senha_padrao,
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
            print(f"Usuário '{username}' criado e adicionado ao grupo 'Aluno'.")

    print(f"{num_usuarios} usuários criados e adicionados ao grupo 'Aluno' com sucesso.")
    
    # Criar o usuário para o grupo "Personal"
    username_personal = "personal"
    senha_personal = "personal123"
    email_personal = "personal@example.com"
    
    if not Usuario.objects.filter(username=username_personal).exists():
        personal_user = Usuario.objects.create_user(
            username=username_personal,
            password=senha_personal,
            first_name="Personal",
            last_name="Trainer",
            email=email_personal,
            data_nascimento=fake.date_of_birth(minimum_age=25, maximum_age=45),
            cpf=fake.cpf(),
            endereco=fake.address()
        )
        personal_user.groups.add(grupo_personal)
        personal_user.save()
        print(f"Usuário '{username_personal}' criado e adicionado ao grupo 'Personal'.")
    else:
        print(f"Usuário '{username_personal}' já existe no sistema.")

    # Criar grupos musculares e exercícios
    grupos_musculares = [
        {'nome': 'Peito', 'exercicios': [
            {'nome': 'Supino Reto', 'descricao': 'Exercício básico para peitoral.'},
            {'nome': 'Supino Inclinado', 'descricao': 'Foca na parte superior do peitoral.'},
            {'nome': 'Fly com Halteres', 'descricao': 'Movimentos de abertura e fechamento com halteres.'},
            {'nome': 'Crucifixo na Máquina', 'descricao': 'Máquina que simula o movimento do fly.'},
            {'nome': 'Flexões', 'descricao': 'Trabalha todo o peitoral, além de ombros e tríceps.'},
        ]},
        {'nome': 'Costas', 'exercicios': [
            {'nome': 'Puxada Frontal', 'descricao': 'Puxada de uma barra para baixo em direção ao peito.'},
            {'nome': 'Remada Curvada com Barra', 'descricao': 'Realiza-se uma remada curvando o tronco.'},
            {'nome': 'Remada Sentada', 'descricao': 'Sentado, puxando a alça em direção ao tronco.'},
            {'nome': 'Levantamento Terra', 'descricao': 'Levantamento de uma barra do chão até a altura dos quadris.'},
            {'nome': 'Pull-Ups', 'descricao': 'Puxa o corpo para cima até o queixo ultrapassar a barra.'},
        ]},
        {'nome': 'Pernas', 'exercicios': [
            {'nome': 'Agachamento Livre', 'descricao': 'Agacha e levanta com a barra apoiada nos ombros.'},
            {'nome': 'Leg Press', 'descricao': 'Empurra uma plataforma com os pés.'},
            {'nome': 'Cadeira Extensora', 'descricao': 'Isola os quadríceps, realizando a extensão do joelho.'},
            {'nome': 'Flexora de Pernas', 'descricao': 'Isola os isquiotibiais, realizando a flexão do joelho.'},
            {'nome': 'Levantamento Terra Romeno', 'descricao': 'Focada nos isquiotibiais e glúteos, com menor flexão do joelho.'},
        ]},
        {'nome': 'Ombros', 'exercicios': [
            {'nome': 'Desenvolvimento com Barra', 'descricao': 'Empurrar a barra para cima, trabalhando todos os deltoides.'},
            {'nome': 'Elevação Lateral', 'descricao': 'Elevar halteres para os lados.'},
            {'nome': 'Elevação Frontal', 'descricao': 'Elevar halteres à frente do corpo.'},
            {'nome': 'Elevação Posterior Inclinada', 'descricao': 'Com o tronco inclinado, eleva-se os halteres para trás.'},
            {'nome': 'Desenvolvimento Arnold', 'descricao': 'Girando os pulsos durante o movimento.'},
        ]},
        {'nome': 'Braços', 'exercicios': [
            {'nome': 'Rosca Direta', 'descricao': 'Flexiona-se o cotovelo para levantar o peso.'},
            {'nome': 'Rosca Martelo', 'descricao': 'Similar à rosca direta, mas com pegada neutra.'},
            {'nome': 'Tríceps Pulley', 'descricao': 'Empurra-se a barra para baixo, focando nos tríceps.'},
            {'nome': 'Supino Fechado', 'descricao': 'Supino com pegada fechada, focando mais nos tríceps.'},
            {'nome': 'Mergulho em Paralelas', 'descricao': 'Abaixa e levanta o corpo entre duas barras paralelas.'},
        ]},
    ]

    for grupo_data in grupos_musculares:
        grupo, created = GrupoMuscular.objects.get_or_create(nome=grupo_data['nome'])
        if created:
            print(f"Grupo Muscular '{grupo.nome}' criado.")

        for exercicio_data in grupo_data['exercicios']:
            Exercicio.objects.get_or_create(
                nome=exercicio_data['nome'],
                descricao=exercicio_data['descricao'],
                grupo=grupo
            )
            print(f"Exercício '{exercicio_data['nome']}' criado para o grupo '{grupo.nome}'.")

    print("Grupos musculares e exercícios criados com sucesso.")

if __name__ == '__main__':
    inicializar_dados()
