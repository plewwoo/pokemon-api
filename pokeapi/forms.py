from django.db.models import fields
from django.forms import ModelForm, TextInput, widgets
from .models import *

class PokemonForm(ModelForm):
    class Meta:
        model = Pokemon
        fields = ['name']
        widgets= {'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'Pokemon Name'})}