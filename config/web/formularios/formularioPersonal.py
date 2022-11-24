#Los formularios de django son clases 

from secrets import choice
from tkinter.tix import Select
from django import forms


class FormularioPersonal(forms.Form): 

    #Creando atributo para cargar el selector

    OPCIONES=(
        (1, 'Cocinero'),
        (2, 'Ayudante'),
        (3, 'Mesero'),
        (4, 'Administrador'),
    )
    
    #Dentro de la clase cada atributo será un input 

    nombreEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=60,
        label="Nombre del empleado"
    )

    apellidoEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=60,
        label="Apellidos del empleado"
    )

    fotoEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        label="Foto del empleado"
    )

    cargoEmpleado=forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        required=True,
        choices=OPCIONES,
        label="Cargo del empleado"
    )

    salarioEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control m-b3'}),
        required=True,
        max_length=20,
        label="Salario del empleado"
    )

    contactoEmpleado=forms.CharField(
        widget=forms.TextInput (attrs={'class':'form-control mb-3'}),
        required=True,
        label="Contacto del empleado"
    )

    