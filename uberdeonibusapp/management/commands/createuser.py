from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from uberdeonibusapp.models import CustomUser  # Ajuste o caminho para o seu modelo CustomUser

class Command(BaseCommand):
    help = 'Cria um novo usuário no Django Admin'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='O nome de usuário do novo usuário')
        parser.add_argument('password', type=str, help='A senha do novo usuário')
        parser.add_argument('nome', type=str, help='O nome do novo usuário')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        first_name = kwargs['nome']

        # Verifica se o usuário já existe
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR(f'O usuário "{username}" já existe.'))
        else:
            user = User.objects.create_user(username=username, password=password, first_name=first_name)
            custom_user = CustomUser.objects.get(email=username)
            custom_user.first_name = first_name
            custom_user.save()
