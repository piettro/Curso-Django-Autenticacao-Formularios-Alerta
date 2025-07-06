from apps.galeria.models import Fotografia
from django import forms
from django.core.exceptions import ValidationError

class FotografiaForm(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada']
        labels = {
            'foto': 'Foto',
            'nome': 'Nome',
            'legenda': 'Legenda',
            'categoria': 'Categoria',
            'descricao': 'Descrição',
            'data_fotografia': 'Data de Registro',
            'usuario': 'Usuário'
        }
        
        widgets = {
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da fotografia'}),
            'legenda': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Legenda da fotografia'}),
            'categoria': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Categoria da fotografia'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição da fotografia'}),
            'data_fotografia': forms.DateInput(
                format= '%d/%m/%Y',
                attrs={
                    'class': 'form-control', 
                    'type': 'date'
                }
            ),
            'usuario': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecione o usuario'})
        }

    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if foto:
            if foto.size > 5 * 1024 * 1024:  # 5 MB limit
                raise ValidationError("A imagem deve ter no máximo 5MB.")
        return foto

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome:
            raise ValidationError("O nome da fotografia é obrigatório.")
        return nome