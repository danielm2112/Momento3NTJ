from django.shortcuts import render
from django.shortcuts import redirect
from web.formularios.formularioPersonal import FormularioPersonal
from web.formularios.formularioEdicionPlatos import FormularioEdicionPlatos
from web.formularios.formularioEdicionEmpleado import FormularioEdicionEmpleados

#Importar el formulario a render
from web.formularios.formularioPlatos import FormularioPlatos
# Create your views here.
#Las vistas en Django son los CONTROLADORES 

from web.models import Platos, Empleado


#Las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

def MenuPlatos(request):

    platosConsultados=Platos.objects.all()

    formulario=FormularioEdicionPlatos()

    diccionarioEnvio={
        'platos': platosConsultados,
        'formulario': formulario 
    }

    return render (request, 'menuPlatos.html', diccionarioEnvio)

def MenuEmpleados(request):


    empleadoConsultados=Empleado.objects.all()

    for empleado in empleadoConsultados:
        print(empleado)

    formulario=FormularioEdicionEmpleados()
    diccionarioEnvio={
        'empleados': empleadoConsultados,

        
    }

    return render (request,'menuEmpleados.html', diccionarioEnvio )

def EditarEmpleado(request, id):
    print(id)
    if request.method=='POST':
        datosDelFormulario=FormularioEdicionEmpleados(request.POST)
        if datosDelFormulario.is_valid():
            datosEmpleado=datosDelFormulario.cleaned_data
            try:
                Empleado.objects.filter(pk=id).update(contacto=datosEmpleado["contactoEmpleado"])
                print("EXITO EDITANDO EL EMPLEADO")

            except Exception as error:
                print("error",error)
        return redirect('menuempleados')

def EditarPlato(request,id):
    print(id)
    #Recibir los datos del formulario y editar mi plato 
    if request.method=='POST':
        datosDelFormulario=FormularioEdicionPlatos(request.POST)
        if datosDelFormulario.is_valid():
            datosPlato=datosDelFormulario.cleaned_data
            try:
                Platos.objects.filter(pk=id).update(precio=datosPlato["precioPlato"])
                print("EXITO EDITANDO EL PLATO")

            except Exception as error:
                
                print("error",error)

    return redirect('menu')


def VistaPlatos(request):

    formulario=FormularioPlatos()
    datosParaTemplate={
        'formularioRegistro':formulario,
        'bandera':False
    }

    #Preguntamos si existe alguna petición de tipo POST asciada a la vista
    if request.method=='POST':
        #Deberíamos capturar los datos del formulario 
        datosDelFormulario=FormularioPlatos(request.POST)
        #Verificarsi los datos llegaron correctamente(VALIDACIONES OK)
        if datosDelFormulario.is_valid():
            #Capturamos la data
            datosPlato=datosDelFormulario.cleaned_data
            print(datosDelFormulario)
            print(datosPlato)
            #creamos un objeto del ripo MODELO PLATO
            platoNuevo=Platos(
                nombre=datosPlato["nombrePlato"],
                descripcion=datosPlato["descripcionPlato"],
                foto=datosPlato["fotoPlato"],
                precio=datosPlato["precioPlato"],
                tipo=datosPlato["tipoPlato"]
            )
            #intentamos llevar el objeto platoNuevo a la BD
            try:
                platoNuevo.save()
                datosParaTemplate["bandera"]=True
                print("EXITO GUARDANDO LOS DATOS")

            except Exception as error:
                datosParaTemplate["bandera"]=False
                print("error",error)

    return render(request, 'platos.html', datosParaTemplate)


def VistaPersonal(request):  

    formulario=FormularioPersonal()
    datosParaTemplate1={
        'formularioPersonal':formulario,
        'bandera':False
    }

    if request.method=='POST':
        datosDelPersonal=FormularioPersonal(request.POST)
        if datosDelPersonal.is_valid():
            datosPersonal=datosDelPersonal.cleaned_data
            print(datosDelPersonal)
            print(datosPersonal)
            personalNuevo=Empleado(
                nombre=datosPersonal["nombreEmpleado"],
                apellidos=datosPersonal["apellidoEmpleado"],
                foto=datosPersonal["fotoEmpleado"],
                cargo=datosPersonal["cargoEmpleado"],
                salario=datosPersonal["salarioEmpleado"],
                contacto=datosPersonal["contactoEmpleado"]
            )
            #intentamos llevar el objeto platoNuevo a la BD
            try:
                personalNuevo.save()
                datosParaTemplate1["bandera"]=True
                print("EXITO GUARDANDO EL EMPLEADO")

            except Exception as error:
                datosParaTemplate1["bandera"]=False
                print("error",error)
            
    return render(request, 'personal.html',datosParaTemplate1)