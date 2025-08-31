from django.db import models

class HeaderLogo(models.Model):
    image = models.ImageField(upload_to='logos/header/', help_text="Logo que aparece no header.")
    link = models.URLField(max_length=200, blank=True, null=True, help_text="Link opcional para o logo.")

    def __str__(self):
        return f"Logo do Header (ID: {self.id})"

class HeroImage(models.Model):
    image = models.ImageField(upload_to='hero_images/', help_text="Imagem principal da home page.")
    link = models.URLField(max_length=200, blank=True, null=True, help_text="Link opcional para a imagem.")
    order = models.PositiveIntegerField(default=0, help_text="Use 0, 1, 2... para definir a ordem de aparição.")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Imagem do Hero (Ordem: {self.order})"

class PartnerLogo(models.Model):
    image = models.ImageField(upload_to='logos/partners/', help_text="Logo dos parceiros no rodapé.")
    link = models.URLField(max_length=200, blank=True, null=True, help_text="Link opcional para o parceiro.")
    order = models.PositiveIntegerField(default=0, help_text="Use 0, 1, 2... para definir a ordem no carrossel.")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Logo de Parceiro (Ordem: {self.order})"