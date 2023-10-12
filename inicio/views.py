                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
from django.template import Template, Context
from django.http import HttpResponse
from django.shortcuts import render
from inicio.forms import formestudiante
from inicio.models import Estudiante
from inicio.forms import formcurso
from inicio.models import Curso
from inicio.forms import formbiblio
from inicio.models import Bibliografia



# Create your views here.

def saludo(request):	
    return render(request,r"C:\Users\59899\OneDrive\MEgaone\Python\Visual\ProyectC10\inicio\templates\inicio\inicio.html")

def prueba1(request):	
    return HttpResponse("Hola Susy")			
    # return render(request,r"C:\inicio\prueba.html")

def crear_estudiante(request):
    return render(request,r"C:\Users\59899\OneDrive\MEgaone\Python\Visual\ProyectC10\inicio\templates\inicio\crear_curso.html")

def crear_curso(request):
    return render(request,r"C:\Users\59899\OneDrive\MEgaone\Python\Visual\ProyectC10\inicio\templates\inicio\crear_curso.html")
	
def crear_biblio(request):
    return render(request,r"C:\Users\59899\OneDrive\MEgaone\Python\Visual\ProyectC10\inicio\templates\inicio\crear_Bibl.html")
	

def formestudianteview(request):	
    if request.method == "POST":	
       Studiante=formestudiante(request.POST)
       
       print(Studiante)
       
       if Studiante.is_valid:
           informacion = Studiante.cleaned_data
           student= Estudiante(informacion["Nombre"])
           student.save()	
           return render(request,"inicio/inicio.html")	
       
    else:
       Studiante = formestudiante()     
       return render(request,"inicio/form_estudiante.html", {"Studiante":Studiante})	

def formcursoview(request):	
    if request.method == "POST":	
       variablecurso=formcurso(request.POST)
       
       print(variablecurso)
       
       if variablecurso.is_valid:
           infocurso = variablecurso.cleaned_data
           variable2curso= Curso(infocurso["Nombre_curso"])
           variable2curso.save()	
           return render(request,"inicio/inicio.html")	
       
    else:
       variablecurso = formcurso()     
       return render(request,"inicio/form_curso.html", {"variablecurso":variablecurso})	
   
def formbiblioview(request):	
    if request.method == "POST":	
       variablebiblio=formbiblio(request.POST)
       
       print(variablebiblio)
       
       if variablebiblio.is_valid:
           infobiblio = variablebiblio.cleaned_data
           variable2biblio= Bibliografia(infobiblio["Libro"],["Editorial"])
           variable2biblio.save()	
           return render(request,"inicio/inicio.html")	
       
    else:
       variablebiblio = formbiblio()     
       return render(request,"inicio/form_biblio.html", {"variablebiblio":variablebiblio})	

def buscarlibroview(request):
    return render(request,"inicio/buscar_libro.html")