from django.contrib import admin
from django.urls import path, include
# from inicio.views  import saludo
from inicio.views import crear_estudiante
from inicio.views import crear_curso
from inicio.views import crear_biblio


urlpatterns = [
   # path(" ", saludo,name="saludo"),
   path("admin/", admin.site.urls),
   path(" " ,include("inicio.urls")),	
   path("admin/",admin.site.urls),	
   path("crear estudiante",crear_estudiante,name="crear estudiante"),
   path("crear curso",crear_estudiante,name="CursoN"),
   path("Asociar Bibliografia",crear_biblio,name="Asociar Libro"),
]	
