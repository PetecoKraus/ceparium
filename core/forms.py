from django import forms

from .models import *

class GenusForm(forms.ModelForm):
    class Meta:
        model = Genus
        fields = ['name']