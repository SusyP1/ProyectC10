
from django import forms

# from django.forms import Form
# from django.forms import ModelForm

class formestudiante(forms.Form):	
    
     Nombre = forms.CharField(max_length=10)
     Email = forms.EmailField()
     
    
class formcurso(forms.Form):		
    Nombre_curso = forms.CharField( max_length=10, required=False)

class formbiblio(forms.Form):	
  Libro = forms.CharField( max_length=50, required=False)
  Editorial = forms.CharField( max_length=50, required=False) 