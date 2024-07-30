import os
import django

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_jsom.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from avaliacoes.models import Avaliacao
from execucoes.models import Execucao
from exercicios.models import Exercicio, GrupoMuscular
from treinos.models import Treino
from usuarios.models import Usuario

def create_group(name, permissions):
    group, created = Group.objects.get_or_create(name=name)
    for perm in permissions:
        app_label, model, codename = perm.split(' ')
        if ContentType.objects.filter(app_label=app_label, model=model).exists():
            content_type = ContentType.objects.get(app_label=app_label, model=model)
            permission = Permission.objects.get(content_type=content_type, codename=codename)
            group.permissions.add(permission)
        else:
            print(f"ContentType não encontrado para {app_label} {model}")
    group.save()

aluno_permissions = [
    'avaliacoes avaliacao view_avaliacao',
    'execucoes execucao view_execucao',
    'exercicios exercicio view_exercicio',
    'exercicios grupomuscular view_grupomuscular',
    'treinos treino view_treino',
    'usuarios usuario view_usuario'
]

personal_permissions = [
    'avaliacoes avaliacao add_avaliacao',
    'avaliacoes avaliacao change_avaliacao',
    'avaliacoes avaliacao delete_avaliacao',
    'avaliacoes avaliacao view_avaliacao',
    'execucoes execucao add_execucao',
    'execucoes execucao change_execucao',
    'execucoes execucao delete_execucao',
    'execucoes execucao view_execucao',
    'exercicios exercicio add_exercicio',
    'exercicios exercicio change_exercicio',
    'exercicios exercicio delete_exercicio',
    'exercicios exercicio view_exercicio',
    'exercicios grupomuscular add_grupomuscular',
    'exercicios grupomuscular change_grupomuscular',
    'exercicios grupomuscular delete_grupomuscular',
    'exercicios grupomuscular view_grupomuscular',
    'treinos treino add_treino',
    'treinos treino change_treino',
    'treinos treino delete_treino',
    'treinos treino view_treino',
    'usuarios usuario add_usuario',
    'usuarios usuario change_usuario',
    'usuarios usuario delete_usuario',
    'usuarios usuario view_usuario'
]

def inicializa_dados():
    # Criar grupos e permissões
    create_group('Aluno', aluno_permissions)
    create_group('Personal', personal_permissions)
    print("Grupos e permissões criados com sucesso!")

    # Dados para serem cadastrados (exemplo de grupos musculares e exercícios)
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
        for exercicio_data in grupo_data['exercicios']:
            Exercicio.objects.get_or_create(
                nome=exercicio_data['nome'],
                descricao=exercicio_data['descricao'],
                grupo=grupo
            )

    print("Dados iniciais cadastrados com sucesso!")

if __name__ == '__main__':
    inicializa_dados()
