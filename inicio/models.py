from django.db import models

# Create your models here.
class Estudiante(models.Model):	
    Nombre=models.CharField(max_length=40)
    Email=models.EmailField()	

class Curso(models.Model):		
    Nombre_curso=models.CharField(max_length=40)		
    Numero=models.IntegerField()
 
 
class Bibliografia(models.Model):	
    Libro=models.CharField(max_length=40)		
    Editorial=models.CharField(max_length=40)
 