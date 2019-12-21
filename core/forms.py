from django.forms import (ModelForm, 
TextInput, 
Textarea, 
EmailInput,
NumberInput
)
from .models import Cliente



class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'email', 'bairro', 'endereco', 'cpf_cnpj')
        widgets = {
            'nome': TextInput(attrs={
                'class':'col-xl-4 col-md-6',
                'placeholder': 'Nome Completo',
                'required': '',
            }),
            'email': EmailInput(attrs={
                'class':'col-xl-4 col-md-6',
                'placeholder':'Email do cliente',
                'required':'',
            }),
            'bairro': TextInput(attrs={
                'class':'col-xl-4 col-md-6',
                'placeholder':'Bairro',
                'required':'',
            }),
            'endereco': TextInput(attrs={
                'class':'col-xl-4 col-md-6',
                'placeholder':'Endereço',
                'required':'',
            }),
            'cpf_cnpj': NumberInput(attrs={
                'class':'col-xl-4 col-md-6',
                'id':'cpf',
                'placeholder':'CPF ou CNPJ do cliente',
                'required':'',
            }),
        }