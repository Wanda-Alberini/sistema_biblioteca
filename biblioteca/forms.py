from django import forms


class LibroFormulario(forms.Form):
    autor = forms.CharField(required=True, max_length=64)
    titulo = forms.CharField(required=True, max_length=64)