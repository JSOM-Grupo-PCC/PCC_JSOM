from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Cria grupos e permissões iniciais para o sistema'

    def handle(self, *args, **options):
        # Criação dos grupos
        personal_group, _ = Group.objects.get_or_create(name='Personal')
        aluno_group, _ = Group.objects.get_or_create(name='Aluno')

        # Permissões para o grupo Personal
        # (supondo que você tenha modelos chamados Programa, Avaliacao, etc.)
        for model in ['programa', 'avaliacao', 'treino', 'exercicio']:
            for perm in ['add', 'change', 'delete', 'view']:
                permission_name = f'{perm}_{model}'
                try:
                    model_perm = Permission.objects.get(codename=permission_name)
                    personal_group.permissions.add(model_perm)
                except Permission.DoesNotExist:
                    print(f'Permissão {permission_name} não encontrada.')

        # Permissões para o grupo Aluno (somente visualização)
        for model in ['programa', 'avaliacao', 'treino', 'exercicio']:
            perm_name = f'view_{model}'
            try:
                model_perm = Permission.objects.get(codename=perm_name)
                aluno_group.permissions.add(model_perm)
            except Permission.DoesNotExist:
                print(f'Permissão {perm_name} não encontrada.')

        self.stdout.write(self.style.SUCCESS('Grupos e permissões criados/atualizados com sucesso!'))
