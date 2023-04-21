from django.contrib import admin
from . import models

admin.site.register(models.Produto)
admin.site.register(models.Marca)
admin.site.register(models.CategoriaSuperior)
admin.site.register(models.CategoriaInferior)
