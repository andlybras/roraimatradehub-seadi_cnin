from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import EmpresaProfileForm, EmpreendedorProfileForm
from .models import EmpresaProfile, EmpreendedorProfile

@login_required
def manage_profile_view(request):
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

    try:
        profile_instance = ProfileModel.objects.get(user=user)
    except ProfileModel.DoesNotExist:
        profile_instance = None

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