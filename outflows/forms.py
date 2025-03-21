from django import forms
from django.core.exceptions import ValidationError
from . import models


class OutflowForm(forms.ModelForm):
    class Meta:
        model = models.Outflow
        fields = ['product', 'quantity_size_p', 'quantity_size_m', 'quantity_size_g', 'quantity_size_gg', 'description', 'payment_type', 'customer_name', 'customer_phone']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity_size_p': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity_size_m': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity_size_g': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity_size_gg': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'payment_type': forms.Select(attrs={'class': 'form-control'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'product': 'Produto',
            'quantity_size_p': 'Quantidade P',
            'quantity_size_m': 'Quantidade M',
            'quantity_size_g': 'Quantidade G',
            'quantity_size_gg': 'Quantidade GG',
            'description': 'Descrição',
            'payment_type': 'Pagamento',
            'customer_name': 'Cliente',
            'customer_phone': 'Telefone'
        }

    def clean_quantity_size_p(self):
        quantity_size_p = self.cleaned_data.get('quantity_size_p')
        product = self.cleaned_data.get('product')

        if quantity_size_p > product.quantity_size_p:
            raise ValidationError(
                f'A quantidade disponível em estoque para o produto {product.title} de tamanho P é de {product.quantity_size_p} unidades.'
            )

        return quantity_size_p

    def clean_quantity_size_m(self):
        quantity_size_m = self.cleaned_data.get('quantity_size_m')
        product = self.cleaned_data.get('product')

        if quantity_size_m > product.quantity_size_m:
            raise ValidationError(
                f'A quantidade disponível em estoque para o produto {product.title} de tamanho M é de {product.quantity_size_m} unidades.'
            )

        return quantity_size_m

    def clean_quantity_size_g(self):
        quantity_size_g = self.cleaned_data.get('quantity_size_g')
        product = self.cleaned_data.get('product')

        if quantity_size_g > product.quantity_size_g:
            raise ValidationError(
                f'A quantidade disponível em estoque para o produto {product.title} de tamanho G é de {product.quantity_size_g} unidades.'
            )

        return quantity_size_g

    def clean_quantity_size_gg(self):
        quantity_size_gg = self.cleaned_data.get('quantity_size_gg')
        product = self.cleaned_data.get('product')

        if quantity_size_gg > product.quantity_size_gg:
            raise ValidationError(
                f'A quantidade disponível em estoque para o produto {product.title} de tamanho GG é de {product.quantity_size_gg} unidades.'
            )

        return quantity_size_gg
