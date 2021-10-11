from django.urls import path

from .views import *

app_name = 'core'

urlpatterns = [
    path('genuses/', GenusListView.as_view(), name='genuses'),
    path('<slug:genus_slug>/species/', SpeciesListView.as_view(), name='species'),
    path('<slug:genus_slug>/<slug:species_slug>/strains/', StrainListView.as_view(), name='strains'),
]