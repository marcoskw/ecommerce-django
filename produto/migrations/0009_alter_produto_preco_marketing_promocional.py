# Generated by Django 4.2 on 2023-05-10 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0008_categoriainferior_categoria_superior_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Preço Promo'),
        ),
    ]