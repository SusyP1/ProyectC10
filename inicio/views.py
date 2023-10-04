                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
from django.template import Template, Context
from django.http import HttpResponse
from django.shortcuts import render
# from forms import Estudiante
# from forms import Curso
# from forms import Bibliografia



# Create your views here.

def saludo(request):	
    return render(request,r"C:\Users\59899\OneDrive\MEgaone\Python\Visual\ProyectC10\inicio\templates\inicio\inicio.html")

def crear_estudiante(request):
    return render(request,r"C:\Users\59899\OneDrive\MEgaone\Python\Visual\ProyectC10\inicio\templates\inicio\crear_estudiante.html",{})

def crear_curso(request):
    return render(request,r"\inicio\crear_curso")
	
def crear_biblio(request):
    return render(request,r"\inicio\crear_Bibl")
	

# def curso_formulario(request):	
#     if request.method == "POST":	
#        curso=Curso(request.post["curso"],(request.post["nombre"])	
#        curso.save()	
#        return render(request,"miApp/inicio.html")	
# return render(request,"miApp/curso_formulario.html")	


