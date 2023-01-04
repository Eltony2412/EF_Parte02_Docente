from django.shortcuts import render,HttpResponse

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

def crear_docente(request):
    return render(request,'crear_docente.html',{
    'titulo': 'Crear Docente'
    })

def listar_docente(request):
    return render(request,'listar_docente.html',{
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