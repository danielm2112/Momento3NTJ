from django import forms


class FormularioEdicionEmpleados(forms.Form):
    
    telefono=forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required=True,
        label="Contacto"
    )