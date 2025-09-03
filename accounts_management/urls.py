from django.urls import path, reverse_lazy
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
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset_form.html',
        email_template_name='emails/password_reset_email.html',
        subject_template_name='emails/password_reset_subject.txt',
        success_url=reverse_lazy('password_reset_done')
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url=reverse_lazy('password_reset_complete')
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]