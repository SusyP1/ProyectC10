"""
URL configuration for Clase10 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import include,path 
 

from inicio.views import saludo
from inicio.views import prueba1
from inicio.views import crear_estudiante
from inicio.views import crear_curso
from inicio.views import crear_biblio
from inicio.views import formestudianteview
from inicio.views import formcursoview
from inicio.views import formbiblioview
from inicio.views import buscarlibroview

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", saludo),
    path("prueba/",prueba1),
    path("crear estudiante/",crear_estudiante,name="crear estudiante"),
    path("Crear curso/",formcursoview,name="CursoN"),
    path("Asociar Bibliografia/",formbiblioview,name="Asociar Libro"),
    path("Formulario estudiante/",formestudianteview,name="Formulario estudiante"),
    path("Busqueda Libro/",buscarlibroview,name="busqueda libro"),
    
]


# # from inicio.views import crear_estudiante
# # from inicio.views import crear_curso
# # from inicio.views import crear_biblio

# # urlpatterns = [
# #    path(" ", saludo,name="saludo"),
# #    path(" " ,include("inicio.urls")),	
# #    path("admin/",admin.site.urls),	
# #    path("crear estudiante",crear_estudiante,name="crear estudiante"),
# #    path("crear curso",crear_estudiante,name="Curso Nuevo"),
# #    path("Asociar Bibliografia",crear_biblio,name="Asociar Libro"),
# # ]