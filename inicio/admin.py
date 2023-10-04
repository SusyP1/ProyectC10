from django.contrib import admin
from inicio.models import Curso
from inicio.models import Estudiante    
from inicio.models import Bibliografia

# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Bibliografia)
