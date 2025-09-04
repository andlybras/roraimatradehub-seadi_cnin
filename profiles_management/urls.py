from django.urls import path
from . import views

urlpatterns = [
    path('dados-empresariais/', views.manage_profile_view, name='manage_profile'),
]