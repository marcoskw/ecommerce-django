from django.contrib import admin
from . import models


class CategoriaServicoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome_categoria_servico',

    ]
    list_display_links = [
        'id',
        'nome_categoria_servico',
    ]

    list_filter = [
        'nome_categoria_servico',
    ]


class ServicoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome_servico',
        'categoria_servico',
        'descricao',
        'get_preco_marketing_formatado',
        'get_preco_marketing_promocional_formatado'
    ]

    list_display_links = [
        'id',
        'nome_servico'
    ]


admin.site.register(models.Servico, ServicoAdmin)
admin.site.register(models.CategoriaServico, CategoriaServicoAdmin)
