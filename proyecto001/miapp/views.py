from django.shortcuts import render,HttpResponse,redirect
from miapp.models import Docente
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html',{
    'titulo': 'Inicio',
    'mensaje' : 'Hola bienvenidos a la pagina'
    })

def integrantes(request):
    estudiantes = [
                    'Carlos Aquino',
                    'Luis Gayoso',
                    'Elberth Luque'
                    ]
    return render(request,'integrantes.html',{
    'titulo': 'Integrantes',
    'estudiantes': estudiantes
    })

def save_docente(request):
    if request.method == 'GET':
        codigo = request.GET['codigo']
        nombre = request.GET['nombre']
        apellido_materno = request.GET['apellido_materno']
        apellido_paterno = request.GET['apellido_paterno']
        dni = request.GET['dni']
        fecha_nacimiento =request.GET['fecha_nacimiento']
        estado = request.GET['estado']
 
        docente = Docente(
            codigo =codigo,
            nombre=nombre,
            apellido_materno=apellido_materno,
            apellido_paterno=apellido_paterno,
            dni=dni,
            fecha_nacimiento=fecha_nacimiento,
            estado=estado,
        )
        docente.save()
        # Crear un mensaje flash (Sesión que solo se muestra 1 vez)
        messages.success(request, f'Se agregó correctamente el artículo {docente.id}')
        return redirect('listar_docente')
    else:
        return HttpResponse("<h2>No se ha podido registrar el artículo</h2>")

def crear_docente(request):
    return render(request,'crear_docente.html',{
    'titulo': 'Crear Docente'
    })

def eliminar_docente(request, id):
    docente = Docente.objects.get(pk=id)
    docente.delete()
    return redirect('listar_docente')

def listar_docente(request):
    docente = Docente.objects.all()
    return render(request,'listar_docente.html',{
    'docentes': docente,
    'titulo': 'Listar Docente'
        })

def crear_curso(request):
    return render(request,'crear_curso.html',{
    'titulo': 'Crear Curso'
    })

def listar_curso(request):
    return render(request,'listar_curso.html',{
    'titulo': 'Listar Curso'
    })