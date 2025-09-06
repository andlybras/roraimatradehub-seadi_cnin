from django import forms
from .models import EmpresaProfile, EmpreendedorProfile, CNAE

class BaseProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.required:
                field.label = f'{field.label} *'
class EmpresaProfileForm(BaseProfileForm):
    declaracao = forms.BooleanField(
        required=True,
        label="Declaro que todas as informações submetidas são verídicas, sob as penas da lei."
    )

    class Meta:
        model = EmpresaProfile
        exclude = ['user']
        labels = {
            'cnae_principal': 'CNAE Principal',
            'logotipo': 'Logotipo',
            'comprovante_dados': 'Comprovante de Dados Empresariais (PDF, JPG)',
            'comprovante_responsavel': 'Comprovante do Responsável Legal (PDF, JPG)',
        }
        widgets = {
            'razao_social': forms.TextInput(attrs={'placeholder': 'Nome da empresa como no registro oficial'}),
            'nome_fantasia': forms.TextInput(attrs={'placeholder': 'Nome popular da empresa'}),
            'cnpj': forms.TextInput(attrs={'placeholder': '00.000.000/0000-00', 'class': 'cnpj-mask'}),
            'inscricao_estadual': forms.TextInput(attrs={'placeholder': 'Apenas números'}),
            'cep': forms.TextInput(attrs={'placeholder': '00000-000', 'id': 'id_cep'}),
            'logradouro': forms.TextInput(attrs={'placeholder': 'Rua, Avenida, etc.', 'id': 'id_logradouro'}),
            'numero': forms.TextInput(attrs={'placeholder': 'Ex: 123 ou S/N'}),
            'complemento': forms.TextInput(attrs={'placeholder': 'Apartamento, Bloco, Sala'}),
            'bairro': forms.TextInput(attrs={'placeholder': 'Bairro', 'id': 'id_bairro'}),
            'cidade': forms.TextInput(attrs={'placeholder': 'Cidade', 'id': 'id_cidade'}),
            'uf': forms.TextInput(attrs={'placeholder': 'UF', 'id': 'id_uf'}),
            'telefone_institucional': forms.TextInput(attrs={'placeholder': '+55 (95) XXXX-XXXX', 'class': 'phone-mask'}),
            'email_institucional': forms.EmailInput(attrs={'placeholder': 'contato@suaempresa.com'}),
            'cnae_principal': forms.Select(attrs={'id': 'id_cnae_principal'}),
            'cnaes_secundarios': forms.SelectMultiple(attrs={'id': 'id_cnaes_secundarios', 'placeholder': 'Pesquise e selecione um ou mais CNAEs'}),
            'responsavel_nome': forms.TextInput(attrs={'placeholder': 'Nome completo do responsável'}),
            'responsavel_email': forms.EmailInput(attrs={'placeholder': 'email@responsavel.com'}),
            'responsavel_telefone': forms.TextInput(attrs={'placeholder': '+55 (95) 9XXXX-XXXX', 'class': 'phone-mask'}),
            'responsavel_cargo': forms.TextInput(attrs={'placeholder': 'Ex: Diretor, Gerente, Sócio-Administrador'}),
            'website': forms.URLInput(attrs={'placeholder': 'https://www.suaempresa.com'}),
            'redes_sociais': forms.TextInput(attrs={'placeholder': 'Link do Instagram, LinkedIn, etc.'}),
        }

class EmpreendedorProfileForm(forms.ModelForm):
    declaracao = forms.BooleanField(
        required=True,
        label="Declaro que todas as informações submetidas são verídicas, sob as penas da lei."
    )
    class Meta:
        model = EmpreendedorProfile
        exclude = ['user']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'placeholder': 'Seu nome completo'}),
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00'}),
            'biografia': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Fale um pouco sobre você e sua atuação profissional...'}),
            'area_atuacao': forms.TextInput(attrs={'placeholder': 'Ex: Consultoria de TI, Artesanato, etc.'}),
            'cidade': forms.TextInput(attrs={'placeholder': 'Sua cidade'}),
            'estado': forms.TextInput(attrs={'placeholder': 'UF'}),
            'telefone_contato': forms.TextInput(attrs={'placeholder': '(95) 90000-0000'}),
            'rede_social_profissional': forms.URLInput(attrs={'placeholder': 'Link do seu perfil no LinkedIn, etc.'}),
        }