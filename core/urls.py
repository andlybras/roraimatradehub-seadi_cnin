from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quero-vender/', views.quero_vender, name='quero_vender'),
]