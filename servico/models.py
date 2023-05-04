from django.db import models


class CategoriaServico(models.Model):
    nome_categoria_servico = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_categoria_servico

    class Meta:
        verbose_name = 'Categoria Serviço'
        verbose_name_plural = 'Categorias Serviços'


class Servico(models.Model):
    nome_servico = models.CharField(max_length=255)
    categoria_servico = models.ForeignKey(
        CategoriaServico, on_delete=models.DO_NOTHING)
    descricao = models.TextField()
    preco_marketing = models.FloatField(verbose_name='Preço')
    preco_marketing_promocional = models.FloatField(
        default=0, verbose_name='Preço Promo')

    def get_preco_marketing_formatado(self):
        return f'R$ {self.preco_marketing:.2f}'.replace('.', ',')
    get_preco_marketing_formatado.short_description = 'Preço'

    def get_preco_marketing_promocional_formatado(self):
        return f'R$ {self.preco_marketing_promocional:.2f}'.replace('.', ',')
    get_preco_marketing_promocional_formatado.short_description = 'Preço Promo'

    def __str__(self):
        return self.nome_servico
