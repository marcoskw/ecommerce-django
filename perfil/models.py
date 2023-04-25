from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
import re
from utils.validacpf import valida_cpf
from utils.validacnpj import valida_cnpj


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    tipo_usuario = models.CharField(
        max_length=1,
        default='C',
        choices=(
            ('C', 'Cliente'),
            ('F', 'Forecedor'),
        )
    )
    nome = models.CharField(max_length=255, blank=True)
    razao_social = models.CharField(max_length=255, blank=True)
    data_nascimento = models.DateField(blank=True)
    cpf_cnpj = models.CharField(max_length=18, blank=True)
    telefone = models.CharField(max_length=13, blank=True)
    endereco = models.CharField(max_length=50, blank=True)
    numero = models.CharField(max_length=5, blank=True)
    complemento = models.CharField(max_length=30, blank=True)
    bairro = models.CharField(max_length=30, blank=True)
    cep = models.CharField(max_length=8, blank=True)
    cidade = models.CharField(max_length=30, blank=True)
    estado = models.CharField(
        max_length=2,
        default='RS',
        blank=True,
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
            ('TO', 'Tocantins')
        )
    )
    obs = models.TextField(blank=True)

    def __str__(self):
        return f'{self.usuario}'

    def clean(self):
        error_messages = {}

        if not valida_cpf(self.cpf_cnpj) or valida_cnpj(self.cpf_cnpj):
            error_messages['cpf_cnpj'] = 'Digite um CPF ou CNPJ válido'

        if re.search(r'[^0-9]', self.cep) or len(self.cep) < 8:
            error_messages['cep'] = 'Digite um CEP válido somente com números'

        if error_messages:
            raise ValidationError(error_messages)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
