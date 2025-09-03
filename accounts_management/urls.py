from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import RegisterView, dashboard, CustomLoginView, activate, resend_activation_email

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(
        template_name='accounts/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
     path('activation-sent/', TemplateView.as_view(
        template_name='accounts/account_activation_sent.html'
    ), name='account_activation_sent'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('activation-valid/', TemplateView.as_view(
        template_name='accounts/account_activation_valid.html'
    ), name='account_activation_valid'),
    path('activation-invalid/', TemplateView.as_view(
        template_name='accounts/account_activation_invalid.html'
    ), name='account_activation_invalid'),
    path('resend-activation/', resend_activation_email, name='resend_activation_email'),
    path('already-active/', TemplateView.as_view(
        template_name='accounts/account_already_active.html'
    ), name='account_already_active'),

]