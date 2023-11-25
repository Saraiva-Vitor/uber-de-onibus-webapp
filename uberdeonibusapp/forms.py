from django import forms
from .models import CustomUser
from validate_docbr import CPF
from datetime import datetime
import re

class CadastroForm(forms.ModelForm):
    confirma_email = forms.EmailField(label='Confirme o Email', required=True)
    confirma_password = forms.CharField(widget=forms.PasswordInput, label='Confirme a Senha', required=True)
    data_nascimento = forms.DateField(
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],  # Formatos aceitos para a data
        widget=forms.DateInput(format='%d/%m/%Y')
    )

    class Meta:
        model = CustomUser
        fields = ['nome', 'cpf', 'data_nascimento', 'email', 'confirma_email', 'telefone', 'password', 'confirma_password',
                  'cep', 'endereco', 'numero', 'complemento', 'estado', 'bairro', 'cidade']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        confirma_email = cleaned_data.get('confirma_email')
        password = cleaned_data.get('password')
        confirma_password = cleaned_data.get('confirma_password')

        # Validação de email e senha
        if email and confirma_email and email != confirma_email:
            self.add_error('confirma_email', 'Emails não conferem.')

        if password and confirma_password and password != confirma_password:
            self.add_error('confirma_password', 'Senhas não conferem.')

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if not CPF().validate(cpf):
            raise forms.ValidationError('CPF inválido')
        return cpf

    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data['data_nascimento']
        return data_nascimento

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        # Aceita apenas números e deve ter pelo menos 10 dígitos
        telefone = re.sub(r'\D', '', telefone)
        if len(telefone) < 10:
            raise forms.ValidationError('Telefone inválido')
        return telefone

    def clean_cep(self):
        cep = self.cleaned_data['cep']
        # Remova o traço do CEP
        cep = cep.replace('-', '')
        return cep
