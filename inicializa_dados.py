import os
import django

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_jsom.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from avaliacoes.models import Avaliacao  # Substitua 'avaliacoes' pelo nome do seu aplicativo
from execucoes.models import Execucao  # Substitua 'execucoes' pelo nome do seu aplicativo
from exercicios.models import Exercicio, GrupoMuscular  # Substitua 'exercicios' pelo nome do seu aplicativo
from treinos.models import Treino  # Substitua 'treinos' pelo nome do seu aplicativo
from usuarios.models import Usuario  # Substitua 'usuarios' pelo nome do seu aplicativo

def create_group(name, permissions):
    group, created = Group.objects.get_or_create(name=name)
    for perm in permissions:
        app_label, model, codename = perm.split(' ')
        content_type = ContentType.objects.get(app_label=app_label, model=model)
        permission = Permission.objects.get(content_type=content_type, codename=codename)
        group.permissions.add(permission)
    group.save()

aluno_permissions = [
    'avaliacoes avaliacao view_avaliacao',
    'execucoes execucao view_execucao',
    'exercicios exercicio view_exercicio',
    'exercicios grupomuscular view_grupomuscular',
    'treinos treino view_treino',
    'usuarios user view_user'
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
    'usuarios user add_user',
    'usuarios user change_user',
    'usuarios user delete_user',
    'usuarios user view_user'
]

def inicializa_dados():
    # Criar grupos e permissões
    create_group('Aluno', aluno_permissions)
    create_group('Personal', personal_permissions)
    print("Grupos e permissões criados com sucesso!")

    # Dados para serem cadastrados
    grupos_musculares = [
        {
            'nome': 'Peito',
            'exercicios': [
                {'nome': 'Supino Reto', 'descricao': 'Exercício básico para peitoral. Realizado deitado em um banco, empurrando a barra para cima.'},
                {'nome': 'Supino Inclinado', 'descricao': 'Foca na parte superior do peitoral. Similar ao supino reto, mas o banco é inclinado.'},
                {'nome': 'Fly com Halteres', 'descricao': 'Movimentos de abertura e fechamento com halteres, trabalhando a parte interna do peito.'},
                {'nome': 'Crucifixo na Máquina', 'descricao': 'Máquina que simula o movimento do fly, isolando os pectorais.'},
                {'nome': 'Flexões', 'descricao': 'Exercício de peso corporal que trabalha todo o peitoral, além de ombros e tríceps.'},
            ]
        },
        {
            'nome': 'Costas',
            'exercicios': [
                {'nome': 'Puxada Frontal', 'descricao': 'Puxada de uma barra para baixo em direção ao peito, focando no latíssimo do dorso.'},
                {'nome': 'Remada Curvada com Barra', 'descricao': 'Com a barra, realiza-se uma remada curvando o tronco, trabalhando a parte superior das costas.'},
                {'nome': 'Remada Sentada', 'descricao': 'Sentado, puxando a alça em direção ao tronco, exercitando a parte média das costas.'},
                {'nome': 'Levantamento Terra', 'descricao': 'Levantamento de uma barra do chão até a altura dos quadris, engajando toda a musculatura das costas.'},
                {'nome': 'Pull-Ups', 'descricao': 'Exercício de peso corporal onde se puxa o corpo para cima até o queixo ultrapassar a barra.'},
            ]
        },
        {
            'nome': 'Pernas',
            'exercicios': [
                {'nome': 'Agachamento Livre', 'descricao': 'Exercício completo para pernas, onde se agacha e levanta com a barra apoiada nos ombros.'},
                {'nome': 'Leg Press', 'descricao': 'Máquina onde se empurra uma plataforma com os pés, trabalhando quadríceps e glúteos.'},
                {'nome': 'Cadeira Extensora', 'descricao': 'Máquina que isola os quadríceps, realizando a extensão do joelho.'},
                {'nome': 'Flexora de Pernas', 'descricao': 'Máquina que isola os isquiotibiais, realizando a flexão do joelho.'},
                {'nome': 'Levantamento Terra Romeno', 'descricao': 'Variante do levantamento terra focada nos isquiotibiais e glúteos, com menor flexão do joelho.'},
            ]
        },
        {
            'nome': 'Ombros',
            'exercicios': [
                {'nome': 'Desenvolvimento com Barra', 'descricao': 'Empurrar a barra para cima, trabalhando todos os deltoides.'},
                {'nome': 'Elevação Lateral', 'descricao': 'Elevar halteres para os lados, focando nos deltoides laterais.'},
                {'nome': 'Elevação Frontal', 'descricao': 'Elevar halteres à frente do corpo, trabalhando os deltoides frontais.'},
                {'nome': 'Elevação Posterior Inclinada', 'descricao': 'Com o tronco inclinado, eleva-se os halteres para trás, focando nos deltoides posteriores.'},
                {'nome': 'Desenvolvimento Arnold', 'descricao': 'Variante do shoulder press, girando os pulsos durante o movimento, trabalhando o deltoide em várias angulações.'},
            ]
        },
        {
            'nome': 'Braços',
            'exercicios': [
                {'nome': 'Rosca Direta', 'descricao': 'Com barra ou halteres, flexiona-se o cotovelo para levantar o peso, focando nos bíceps.'},
                {'nome': 'Rosca Martelo', 'descricao': 'Similar à rosca direta, mas com pegada neutra, trabalhando bíceps e braquiorradial.'},
                {'nome': 'Tríceps Pulley', 'descricao': 'Com cabo na polia, empurra-se a barra para baixo, focando nos tríceps.'},
                {'nome': 'Supino Fechado', 'descricao': 'Supino com pegada fechada, focando mais nos tríceps.'},
                {'nome': 'Mergulho em Paralelas', 'descricao': 'Exercício de peso corporal onde se abaixa e levanta o corpo entre duas barras paralelas, trabalhando tríceps, peito e ombros.'},
            ]
        },
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
