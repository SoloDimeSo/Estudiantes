from django.db import models

# Create your models here.

class Estudiantes(models.Model):
    rut =   models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    fecha_nac = models.DateField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    modificacion_registro = models.DateTimeField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    
class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False, blank=False)
    numero = models.IntegerField(blank=False, null=False, default=0)
    dpto = models.CharField(max_length=10, null=True, blank=True)
    comuna = models.CharField(max_length=10, blank=True, null=True)
    ciudad = models.CharField(max_length=10, blank=True, null=True)
    region = models.CharField(max_length=10, blank=True, null=True)
    estudiante_id = models.OneToOneField(Estudiantes, unique=True, blank=False, null=False, on_delete=models.CASCADE)
    
    
class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    activo = models.BooleanField(default=True)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    modificacion_registro = models.DateTimeField(auto_now=True)
    creado_por = models.CharField(max_length=50)

class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    version = models.IntegerField(default=1, blank=False, null=False) 
    profesor_id = models.ManyToManyField('Profesor')
    estudiante_id = models.ManyToManyField('Estudiantes')