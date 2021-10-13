from django import forms

from .models import *

class GenusForm(forms.ModelForm):
    class Meta:
        model = Genus
        fields = ['name']


class SpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = ['name']


class StrainForm(forms.ModelForm):
    class Meta:
        model = Strain
        fields = ['strain_name', 'access_number', 'taxon_rank', 'collection_date', 
                'reactivation_date', 'preparation', 'photo', 'collection_place',
                'collection_point', 'isolated_by', 'identified_by']