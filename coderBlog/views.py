from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context,loader

from coderBlog.models import *
from coderBlog.forms import *


# Create your views here.


def clientes(request):
    
    clientes = Clientes()
    clientes.save()
    
    texto = f'Cliente:{clientes.nombre}, {clientes.apellido}, {clientes.email} '
    return render(request, 'coderBlog/clientes.html')

def programadores(request):
    programadores = Programadores()
    programadores.save()
     
    texto = f'Programador: {programadores.nombre}, {programadores.apellido}, {programadores.curso}'
    return render(request, 'coderBlog/programadores.html')

''' 
def profesores(request):
      profesores = Profesores()
      profesores.save()
      
      texto = f'Profesor: {profesores.nombre}, {profesores.apellido}'
      return render(request,'coderBlog/profesores.html')
'''

def profesores(request):
    
    if request.method == "POST":
        #leer los datos del post
        datosProfesor = ProfesoresFormularior(request.POST)
        
        print(datosProfesor)
        if datosProfesor.is_valid:
            
            datos = datosProfesor.cleaned_data
            
            nombre = datos.get("nombre")
            apellido = datos.get("apellido")
            
            profesor = Profesores(nombre=nombre, apellido=apellido)
            profesor.save()
            
            return render(request, 'index.html')         
    
    else:
        profesoresFormulario = ProfesoresFormulario()
        
    return render(request, 'crearProfesor.html', {'profesoresFormulario': profesoresFormulario})


def index(request):
    return render(request, 'coderBlog/index.html')


def formulario(request):
    
    if request.method == "POST":
        
        nombre = request.POST.get('clientes')
        nombre = request.POST.get('programadores')
        nombre = request.POST.get('profesores')
        
        clientes = Clientes(nombre=nombre)
        clientes.save()
        
        programadores = Programadores(nombre=nombre)
        programadores.save()
        
        profesores = Profesores(nombre=nombre)
        profesores.save()
        
        return render(request, 'index.html')
    else:
        return render(request, 'formulario.html')
'''

def formulario(request):
    
    if request.method == "POST":
        
        formulario = Formulario(request.POST)  
        
        #print('formulario')
        #print(formulario)
        
        print(f'is valid: {formulario.is_valid}')
        if formulario.is_valid():
            
            datos = formulario.cleaned_data
            
            nombre = datos.get('clientes','programadores','profesores')
            
            nombre = Clientes(nombre= nombre)
            nombre.save()
            
            nombre = Programadores(nombre=nombre)
            nombre.save()
            
            nombre = Profesores(nombre=nombre)
            nombre.save()
            
            return render(request, 'index.html')
    else: 
        formulario = Formulario()        
    return render(request, 'formulario.html', {'formulario': formulario}) 
'''
def busqueda_nombre(request):
    
    if request.method == 'GET':
        nombre = request.GET.get('nombre')
        print(f'Vamos a buscar el nombre: {nombre}')
    
    return render(request, 'busqueda_nombre.html')

def leer_profesores(request):
    profesores = Profesores.objects.all()
    contexto = {'profesores': profesores}
    return render(request, 'leer_profesores.html', contexto) 
     
def leer_clientes(request):
    clientes = Clientes.objects.all()
    contexto = {'clientes': clientes}
    return render(request, 'leer_clientes.html', contexto) 
    
    
def leer_programadores(request):
    programadores = Programadores.objects.all()
    contexto = {'programadores': programadores}
    return render(request, 'leer_programadores.html', contexto) 
         
def eliminar_profesor(request, nombre_profesor):
    profesor = Profesores.objects.get(nombre=nombre_profesor)
    profesor.delete()
    profesores = Profesores.objects.all()
    contexto= {"profesores":profesores}
    
    return render(request, "leer_profesores", contexto)
      