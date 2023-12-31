from django import forms
from film.models import Film
class movieform(forms.ModelForm): #form definition
    class Meta:
        model=Film
        fields='__all__'
