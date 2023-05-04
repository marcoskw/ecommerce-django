from django.urls import path
from . import views

app_name = 'servico'

urlpatterns = [
    path('', views.ListaServicos.as_view(), name='lista'),
    path('<slug>', views.DetalheServico.as_view(), name='detalhe'),
    path('adicionaraocarrinho/', views.AdicionarAoCarrinho.as_view(),
         name='adicionaraocarrinho'),
    path('removerdocarrinho/', views.RemoverDoCarrinho.as_view(),
         name='removerdocarrinho'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'),
    path('finalizar/', views.Finalizar.as_view(), name='finalizar'),
]
