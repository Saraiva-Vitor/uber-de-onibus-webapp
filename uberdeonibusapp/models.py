from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.contrib.auth.models import AbstractUser
import re

class State(models.Model):
    estado = models.CharField(
        max_length=2,
        default='RJ',
        choices=(
            ('ES', 'Espírito Santo'),
            ('MG', 'Minas Gerais'),
            ('RJ', 'Rio de Janeiro'),
            ('SP', 'São Paulo'),
        ))

    def __str__(self):
        return self.estado
    
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

class Location(models.Model):
    estado = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)
    image = models.ImageField(upload_to='images/locations/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Localidade'
        verbose_name_plural = 'Localidades'

class BusType(models.Model):
    nome_tipo = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome_tipo
    
    class Meta:
        verbose_name = 'Tipo de Ônibus'
        verbose_name_plural = 'Tipos de Ônibus'
    
class Driver(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Motorista'
        verbose_name_plural = 'Motoristas'
    
class Bus(models.Model):
    tipo_onibus = models.ForeignKey(BusType, on_delete=models.CASCADE)
    placa_onibus = models.CharField(max_length=20)
    motorista = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.placa_onibus} - {self.tipo_onibus} ({self.motorista})'
    
    class Meta:
        verbose_name = 'Ônibus'
        verbose_name_plural = 'Ônibus'

class BusRoute(models.Model):
    name = models.CharField(max_length=100)
    origin = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name='origin_routes')
    destination = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name='destination_routes')
    bus = models.ForeignKey(
        Bus, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.origin} to {self.destination})'
    
    class Meta:
        verbose_name = 'Rota'
        verbose_name_plural = 'Rotas'

class BusSchedule(models.Model):
    route = models.ForeignKey(BusRoute, on_delete=models.CASCADE)
    schedule = models.DateTimeField()

    def __str__(self):
        return f"{self.route.name} - {self.schedule}"
    
    class Meta:
        verbose_name = 'Horário'
        verbose_name_plural = 'Horários'

class BusSchedules(models.Model):
    route = models.ForeignKey(BusRoute, on_delete=models.SET_NULL, null=True, blank=True)
    schedule = models.DateTimeField()

    def __str__(self):
        return f"Horário para a rota: {self.route.name} - {self.schedule}"

    class Meta:
        verbose_name = 'Horário'
        verbose_name_plural = 'Horários'

def valida_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        return False

    # Elimina os dois últimos digitos do CPF
    novo_cpf = cpf[:-2]
    reverso = 10                        # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:                   # Primeiro índice vai de 0 a 9,
            index -= 9                  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1                    # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                   # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0                   # Zera o total
            novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequências avaliavam como verdadeiro, então também
    # adicionei essa checagem aqui
    if cpf == novo_cpf and not sequencia:
        return True
    else:
        return False


class CustomUser(AbstractUser):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=15)
    senha = models.CharField(max_length=100)
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(
        max_length=2,
        default='RJ',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )

    def __str__(self):
        return f'{self.usuario}'

    def clean(self):
        error_messages = {}

        cpf_enviado = self.cpf or None
        cpf_salvo = None
        perfil = CustomUser.objects.filter(cpf=cpf_enviado).first()

        if perfil:
            cpf_salvo = perfil.cpf

            if cpf_salvo is not None and self.pk != perfil.pk:
                error_messages['cpf'] = 'CPF já existe.'

        if not valida_cpf(self.cpf):
            error_messages['cpf'] = 'Digite um CPF válido'

        if re.search(r'[^0-9]', self.cep) or len(self.cep) < 8:
            error_messages['cep'] = 'CEP inválido, digite os 8 digitos do CEP.'

        if error_messages:
            raise ValidationError(error_messages)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

CustomUser._meta.get_field('groups').remote_field.related_name = 'customuser_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'customuser_permissions'