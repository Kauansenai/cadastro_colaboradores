from django import forms
from .models import Emprestimo, Colaborador, Equipamento

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['colaborador', 'equipamento', 'quantidade']

    def __init__(self, *args, **kwargs):
        super(EmprestimoForm, self).__init__(*args, **kwargs)
        # Filtra a lista de colaboradores e equipamentos
        self.fields['colaborador'].queryset = Colaborador.objects.all()
        self.fields['equipamento'].queryset = Equipamento.objects.all()

        # Adicionando classes CSS para estilização (opcional)
        self.fields['colaborador'].widget.attrs.update({'class': 'form-control'})
        self.fields['equipamento'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantidade'].widget.attrs.update({'placeholder': 'Quantidade'})

        
