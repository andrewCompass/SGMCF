from django.contrib import admin

from django.urls import path

from pessoas.models import Afiliado
from armazem.models import EstoqueIndividual

# Register your models here.

@admin.register(EstoqueIndividual)
class EstoqueIndividualAdmin(admin.ModelAdmin):
    list_display = ('produto', 'afiliado', 'quantidade')
    search_fields = ('produto__nome', 'afiliado__nome')
    list_filter = ('afiliado', 'produto')
    ordering = ('produto__nome',)
    list_per_page = 10
    empty_value_display = '- vazio -'

    # def has_add_permission(self, request):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False

class EstoqueIndividualInline(admin.TabularInline):
    model = EstoqueIndividual
    extra = 0
    verbose_name = "Estoque Individual"
    verbose_name_plural = "Estoques Individuais"
    fields = ('produto', 'quantidade')
    readonly_fields = ('produto', 'quantidade')

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Afiliado)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'email', 'telefone')
    search_fields = ('nome', 'sobrenome', 'cpf', 'email', 'telefone')
    ordering = ('nome',)
    inlines = [EstoqueIndividualInline]