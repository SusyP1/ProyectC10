
from django import forms

# from django.forms import Form
# from django.forms import ModelForm

class formestudiante(forms.Form):	
    
     Nombre = forms.CharField(max_length=10)
     Email = forms.EmailField()
     
    
# class Curso(forms.Form):		
#     Nombre_curso = forms.charfield( max_length=25, required=False)		
    
# class Bibliografia(forms.Form):	
#     Libro = forms.charfield( max_length=50, required=False)
 