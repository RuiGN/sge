from django import forms
from . import models


class InflowForm(forms.ModelForm):

    class Meta:
        model = models.Inflow
        fields = ['supplier', 'product', 'quantity_size_p', 'quantity_size_m', 'quantity_size_g', 'quantity_size_gg', 'description']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity_size_p': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity_size_m': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity_size_g': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity_size_gg': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'supplier': 'Fornecedor',
            'product': 'Produto',
            'quantity_size_p': 'Quantidade P',
            'quantity_size_m': 'Quantidade M',
            'quantity_size_g': 'Quantidade G',
            'quantity_size_gg': 'Quantidade GG',
            'description': 'Descrição',
        }
