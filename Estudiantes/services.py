from .models import Estudiantes, Profesor, Curso, Direccion
from datetime import date


def crear_curso(codigo, nombre, version):
    nuevo_curso = Curso(codigo=codigo, nombre=nombre, version=version)
    nuevo_curso.save()
    return nuevo_curso
    


def crear_profesor(rut, nombre, apellido):
    nuevo_profesor = Profesor(rut=rut, nombre=nombre, apellido=apellido)
    nuevo_profesor.save()
    return nuevo_profesor


def crear_estudiante(rut, nombre, apellido, fecha_nac,):
    nuevo_estudiante = Estudiantes(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac)
    nuevo_estudiante.save()
    return nuevo_estudiante
    
def crear_direccion(calle,numero,dpto,comuna,ciudad,region,estudiante_id):
    estudiante = Estudiantes.objects.get(rut=estudiante_id)
    nueva_direccion = Direccion(calle=calle,numero=numero,dpto=dpto,comuna=comuna,ciudad=ciudad,region=region,estudiante_id=estudiante)
    nueva_direccion.save()
    return nueva_direccion


def obtiene_estudiante(rut):
    estudiante = Estudiantes.objects.get(rut=rut)
    print(f'[RUT]: {estudiante.rut} Nombres: {estudiante.nombre} Apellidos: {estudiante.apellido}')


def obtiene_profesor(rut):
    profesor = Profesor.objects.get(rut = rut)
    print(f'[RUT]: {profesor.rut} Nombres: {profesor.nombre} Apellidos: {profesor.apellido}')


def obtiene_curso(codigo):
    curso = Curso.objects.get(codigo = codigo)
    print(f'[CODIGO]: {curso.codigo} Nombres: {curso.nombre} Version: {curso.version}')


def agrega_profesor_a_curso(codigo, rut):   
    curso = Curso.objects.get(codigo=codigo)
    profesor = Profesor.objects.get(rut=rut)
    curso.profesor_id.add(profesor)
    curso.save()
    return ' Se ha agregado el profesor al curso '
    


def agrega_cursos_a_estudiante(codigo,rut):
    estudiante = Estudiantes.objects.get(rut=rut)
    cursos = Curso.objects.get(codigo=codigo)
    cursos.estudiante_id.add(estudiante)
    cursos.save()
    return ' Se ha agregado el estudiante al curso '


def imprime_estudiante_cursos(rut):
    
    try:
        estudiante = Estudiantes.objects.get(rut=rut)  
        cursos = curso.estudiante_id.all()
        for curso in cursos: 
            print(curso)
                
            
    except Estudiantes.DoesNotExist:
            print('El estudiante no existe')
    
