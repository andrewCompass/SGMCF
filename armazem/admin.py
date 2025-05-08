from django.contrib import admin

from .models import Categoria, Produto, Estoque, HistoricoEstoque, EstoqueIndividual

from django_modal_actions import ModalActionMixin, modal_action
from django import forms

from pessoas.models import Afiliado


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
    ordering = ('nome',)
    list_per_page = 10
    empty_value_display = '- vazio -'

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria')
    search_fields = ('nome',)
    list_filter = ('categoria',)
    ordering = ('nome',)
    list_per_page = 10
    empty_value_display = '- vazio -'

@admin.register(HistoricoEstoque)
class HistoricoEstoqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'afiliado', 'produto', 'peso', 'data')
    search_fields = ('produto__nome',)
    list_filter = ('tipo', 'afiliado')
    ordering = ('-data',)
    list_per_page = 10
    empty_value_display = '- vazio -'

    def has_add_permission(self, request):
        return False


class ApprovalForm(forms.Form):

    afiliado = forms.ModelChoiceField(
        queryset=Afiliado.objects.all(),
        label="Afiliado",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    tipo = forms.ChoiceField(
        choices=[('entrada', 'Entrada'), ('saida', 'Saída')],
        label="Tipo",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    quantidade = forms.DecimalField(
        max_digits=10,
        decimal_places=3,
        label="Quantidade (Kg)",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

@admin.register(Estoque)
class EstoqueAdmin(ModalActionMixin, admin.ModelAdmin):
    list_display = ('produto', 'quantidade')
    search_fields = ('produto__nome',)
    ordering = ('produto__nome',)
    list_per_page = 10
    empty_value_display = '- vazio -'
    readonly_fields = ('quantidade',)

    modal_actions = ["alterar"]

    @modal_action(
        modal_header="Alterar Estoque",
        modal_description="Preencha os campos abaixo para alterar o estoque.",
        form_class=ApprovalForm
    )
    def alterar(self, request, obj, form_data=None):
        afiliado = form_data['afiliado']
        tipo = form_data['tipo']
        quantidade = form_data['quantidade']

        try:
            estoque_individual = EstoqueIndividual.objects.get(produto=obj.produto, afiliado=afiliado)
        except EstoqueIndividual.DoesNotExist:
            estoque_individual = EstoqueIndividual(produto=obj.produto, afiliado=afiliado, quantidade=0)

        if tipo == 'entrada':
            obj.quantidade += quantidade
            estoque_individual.quantidade += quantidade
        else:
            if obj.quantidade < quantidade:
                raise forms.ValidationError("Quantidade insuficiente no estoque.")

            if estoque_individual.quantidade < quantidade:
                raise forms.ValidationError("Quantidade insuficiente no estoque individual.")

            estoque_individual.quantidade -= quantidade
            obj.quantidade -= quantidade

        historico = HistoricoEstoque(
            tipo=tipo,
            afiliado=afiliado,
            produto=obj.produto,
            peso=quantidade
        )

        historico.save()
        estoque_individual.save()
        obj.save()

        return "Estoque alterado com sucesso."

    alterar.short_description = "Alterar Estoque"
