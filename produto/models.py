from django.conf import settings
import os
from PIL import Image
from django.db import models
from django.utils.text import slugify
from utils import utils


class Marca(models.Model):
    nome_marca = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_marca


class CategoriaSuperior(models.Model):
    nome_categoria_superior = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_categoria_superior

    class Meta:
        verbose_name = 'Categoria Superior'
        verbose_name_plural = 'Categorias Superiores'


class CategoriaInferior(models.Model):
    categoria_superior = models.ForeignKey(
        CategoriaSuperior, on_delete=models.CASCADE, blank=True, null=True)
    nome_categoria_inferior = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_categoria_inferior

    class Meta:
        verbose_name = 'Categoria Inferior'
        verbose_name_plural = 'Categorias Inferiores'


class Produto(models.Model):
    nome_produto = models.CharField(max_length=255)
    nome_marca = models.ForeignKey(
        Marca, on_delete=models.DO_NOTHING, verbose_name='Marca')
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField(max_length=255)
    categoria_superior = models.ForeignKey(
        CategoriaSuperior, on_delete=models.DO_NOTHING)
    categoria_inferior = models.ForeignKey(
        CategoriaInferior, on_delete=models.DO_NOTHING)
    imagem = models.ImageField(
        upload_to='produtos_imagens/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.FloatField(verbose_name='Preço')
    preco_marketing_promocional = models.FloatField(
        default=0, verbose_name='Preço Promo')
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variável'),
            ('S', 'Simples'),
        )
    )

    def get_preco_marketing_formatado(self):
        return utils.formatar_preco(self.preco_marketing)
    get_preco_marketing_formatado.short_description = 'Preço'

    def get_preco_marketing_promocional_formatado(self):
        return utils.formatar_preco(self.preco_marketing_promocional)
    get_preco_marketing_promocional_formatado.short_description = 'Preço Promo'

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_heigt = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_heigt) * original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome_produto)}'
            self.slug = slug
        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome_produto


class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    referencia = models.CharField(max_length=50)
    cod_barras = models.CharField(max_length=13)
    nome_variacao = models.CharField(max_length=255, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome_variacao or self.produto.nome_produto

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
