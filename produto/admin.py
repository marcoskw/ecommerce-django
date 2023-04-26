from django.contrib import admin
from . import models


class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1


class CategoriaSuperiorInline(admin.TabularInline):
    model = models.CategoriaInferior
    extra = 1


class CategoriaInferiorAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome_categoria_inferior',
        'categoria_superior',

    ]
    list_display_links = [
        'id',
        'nome_categoria_inferior',
    ]

    list_filter = [
        'categoria_superior',
    ]


class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        'nome_produto',
        'nome_marca',
        'categoria_superior',
        'categoria_inferior',
        'get_preco_marketing_formatado',
        'get_preco_marketing_promocional_formatado'
    ]
    inlines = [
        VariacaoInline
    ]


admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Marca)
admin.site.register(models.CategoriaSuperior)
admin.site.register(models.CategoriaInferior, CategoriaInferiorAdmin)
admin.site.register(models.Variacao)
