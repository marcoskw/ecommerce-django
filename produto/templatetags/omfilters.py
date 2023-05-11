from django.template import Library
from utils import utils
register = Library()


@register.filter
def formatar_preco(valor):
    return utils.formatar_preco(valor)
