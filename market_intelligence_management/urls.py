from django.urls import path
from . import views

app_name = 'market_intelligence_management'

urlpatterns = [
    path('', views.inteligencia_mercado_view, name='dashboard'),
    path('initial-view/', views.get_initial_view, name='get_initial_view'), # NOVA ROTA
    path('cards/<str:categoria>/', views.listar_cards_por_categoria_view, name='listar_cards'),
    path('card/<int:card_id>/', views.detalhar_card_view, name='detalhar_card'),
    path('glossario/', views.glossario_view, name='glossario'),
]