#Los formularios de django son clases 

from secrets import choice
from tkinter.tix import Select
from django import forms


class FormularioPlatos(forms.Form): 

    #Creando atributo para cargar el selector

    OPCIONES=(
        (1, 'Entrada'),
        (2, 'Plato Fuerte'),
        (3, 'Postre')
    )
    
    #Dentro de la clase cada atributo será un input 

    nombrePlato=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=50,
        label="Nombre del plato"
    )

    descripcionPlato=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control m-b3'}),
        required=False,
        max_length=200,
        label="Descripción del plato"
    )

    fotoPlato=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        label="Foto del plato"
    )

    precioPlato=forms.CharField(
        widget=forms.NumberInput (attrs={'class':'form-control mb-3'}),
        required=True,
        label="Precio del plato"
    )

    tipoPlato=forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        required=True,
        choices=OPCIONES,
        label="Tipo de plato"
    )