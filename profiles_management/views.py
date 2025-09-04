from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import EmpresaProfileForm, EmpreendedorProfileForm
from .models import EmpresaProfile, EmpreendedorProfile

@login_required
def manage_profile_view(request):
    """
    View para criar e editar o perfil do usuário logado.
    Ela identifica o tipo de usuário e apresenta o formulário correspondente.
    """
    user = request.user
    
    if user.user_type == 'empresa':
        ProfileModel = EmpresaProfile
        ProfileForm = EmpresaProfileForm
    elif user.user_type == 'empreendedor':
        ProfileModel = EmpreendedorProfile
        ProfileForm = EmpreendedorProfileForm
    else:
        messages.error(request, 'Tipo de perfil de usuário inválido.')
        return redirect('dashboard')

    # --- CORREÇÃO APLICADA AQUI ---
    # Trocamos get_object_or_404 por uma busca padrão com try/except.
    # Isso permite que a view continue se o perfil não for encontrado.
    try:
        profile_instance = ProfileModel.objects.get(user=user)
    except ProfileModel.DoesNotExist:
        profile_instance = None # Para novos usuários, o perfil será None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile_instance)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            
            messages.success(request, 'Seus dados foram salvos com sucesso!')
            return redirect('dashboard')
    
    else:
        form = ProfileForm(instance=profile_instance)

    context = {
        'form': form
    }
    
    return render(request, 'profiles_management/manage_profile.html', context)