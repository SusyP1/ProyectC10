                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
from django.template import Template, Context
from django.http import HttpResponse
from django.shortcuts import render
from inicio.forms import formestudiante
from inicio.models import Estudiante

# from forms import Curso
# from forms import Bibliografia


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

    
