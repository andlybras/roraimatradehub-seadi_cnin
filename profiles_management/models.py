from django.db import models
from accounts_management.models import CustomUser

# Modelo para armazenar os códigos CNAE
class CNAE(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"

    class Meta:
        verbose_name = "Código CNAE"
        verbose_name_plural = "Banco CNAE"
        ordering = ['codigo']

# Modelo para o Perfil de Empresa
class EmpresaProfile(models.Model):
    # Relacionamento um-para-um com o usuário. Cada usuário só pode ter um perfil.
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='empresa_profile')

    # Dados Empresariais
    razao_social = models.CharField(max_length=255, verbose_name="Razão Social")
    nome_fantasia = models.CharField(max_length=255, verbose_name="Nome Fantasia")
    cnpj = models.CharField(max_length=18, unique=True, verbose_name="CNPJ") # Formato XX.XXX.XXX/XXXX-XX
    inscricao_estadual = models.CharField(max_length=20, verbose_name="Inscrição Estadual")
    
    # Endereço Principal
    cep = models.CharField(max_length=9, verbose_name="CEP") # Formato XXXXX-XXX
    logradouro = models.CharField(max_length=255, verbose_name="Logradouro")
    numero = models.CharField(max_length=20, verbose_name="Número")
    complemento = models.CharField(max_length=100, blank=True, null=True, verbose_name="Complemento")
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    # Contato Institucional
    telefone_institucional = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone Institucional")
    email_institucional = models.EmailField(max_length=255, verbose_name="E-mail Institucional")

    # Dados da Área de Atuação
    cnae_principal = models.ForeignKey(CNAE, on_delete=models.SET_NULL, null=True, related_name='empresas_principal', verbose_name="CNAE Principal")
    cnaes_secundarios = models.ManyToManyField(CNAE, related_name='empresas_secundarias', blank=True, verbose_name="CNAEs Secundários")

    # Dados do Responsável Legal/Delegado
    responsavel_nome = models.CharField(max_length=255, verbose_name="Nome Completo do Responsável")
    responsavel_email = models.EmailField(max_length=255, verbose_name="E-mail do Responsável")
    responsavel_telefone = models.CharField(max_length=20, verbose_name="Telefone/WhatsApp do Responsável")
    responsavel_cargo = models.CharField(max_length=100, verbose_name="Cargo/Função do Responsável")

    # Dados Complementares
    logotipo = models.ImageField(upload_to='logotipos/', verbose_name="Logotipo")
    website = models.URLField(max_length=255, blank=True, null=True)
    redes_sociais = models.CharField(max_length=255, blank=True, null=True, verbose_name="Redes Sociais (links separados por vírgula)")

    # Comprovantes
    comprovante_dados = models.FileField(upload_to='comprovantes/empresa/', verbose_name="Comprovante de Dados Empresariais (PDF, JPG)")
    comprovante_responsavel = models.FileField(upload_to='comprovantes/responsavel/', verbose_name="Comprovante do Responsável Legal (PDF, JPG)")

    def __str__(self):
        return self.nome_fantasia
    
    class Meta:
        verbose_name = "Perfil de Empresa"
        verbose_name_plural = "Dados Empresariais - Empresa"


# Modelo para o Perfil de Empreendedor
class EmpreendedorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='empreendedor_profile')
    
    nome_completo = models.CharField(max_length=255, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF") # Formato XXX.XXX.XXX-XX
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True, verbose_name="Foto de Perfil")
    biografia = models.TextField(verbose_name="Biografia / Resumo Profissional")
    area_atuacao = models.CharField(max_length=150, verbose_name="Área de Atuação")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    estado = models.CharField(max_length=2, verbose_name="Estado (UF)")
    telefone_contato = models.CharField(max_length=20, verbose_name="Telefone/WhatsApp para Contato")
    rede_social_profissional = models.URLField(max_length=255, blank=True, null=True, verbose_name="Link para Rede Social Profissional (LinkedIn, etc.)")

    def __str__(self):
        return self.nome_completo
    
    class Meta:
        verbose_name = "Perfil de Empreendedor"
        verbose_name_plural = "Dados Empresariais - Empreendedor"