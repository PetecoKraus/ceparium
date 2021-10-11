from django.shortcuts import render
from django.views import generic

from .models import *

class GenusListView(generic.ListView):
    template_name = 'ceparium/genuses.html'
    context_object_name = 'genuses_list'

    def get_queryset(self):
        return Genus.objects.order_by('name')[:20]


class SpeciesListView(generic.ListView):
    model = Species
    template_name = 'ceparium/species.html'
    context_object_name = 'species_list'

    def get_queryset(self):
        return Species.objects.filter(genus__slug=self.kwargs['genus_slug']).order_by('name')[:20]

    def get_context_data(self, **kwargs):
        context = super(SpeciesListView, self).get_context_data(**kwargs)
        context['genus_id'] = Genus.objects.filter(slug=self.kwargs['genus_slug'])[0].pk
        context['genus_name'] = Genus.objects.filter(slug=self.kwargs['genus_slug'])[0].name
        context['genus_slug'] = Genus.objects.filter(slug=self.kwargs['genus_slug'])[0].slug
        return context


class StrainListView(generic.ListView):
    model = Strain
    template_name = 'ceparium/strains.html'
    context_object_name = 'strains_list'

    def get_queryset(self):
        return Strain.objects.filter(species__slug=self.kwargs['species_slug']).order_by('strain_name')[:20]

    def get_context_data(self, **kwargs):
        context = super(StrainListView, self).get_context_data(**kwargs)
        context['species_id'] = Species.objects.filter(slug=self.kwargs['species_slug'])[0].pk
        context['species_name'] = Species.objects.filter(slug=self.kwargs['species_slug'])[0].name
        context['genus_slug'] = self.kwargs['genus_slug']
        return context