from django.contrib import admin
from django.urls import path, include
from inicio.views  import saludo
from inicio.views import crear_estudiante

urlpatterns = [
     path(" ", saludo,name="saludo"),
    path("admin/", admin.site.urls),
 
 ]
urlpatterns = [	
path(" " ,include("inicio.urls")),	
path("admin/",admin.site.urls),	
path("crear_estudiante"/<str:nombre>, crear_estudiante,name="crear estudiante")
]	
