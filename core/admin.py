from django.contrib import admin
from .models import Cargo,Servico,Funcionario,Features, Sobre

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico','icone','ativo', 'modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo')

@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('servico', 'descricao', 'icone')

@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = ('estatistica', 'infromacao')