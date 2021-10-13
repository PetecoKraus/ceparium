from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from djgeojson.views import GeoJSONLayerView

from .views import *
from .models import Strain

app_name = 'core'

urlpatterns = [
    path('genuses/', 
        GenusListView.as_view(), name='genuses'),
    path('<slug:genus_slug>/species/', 
        SpeciesListView.as_view(), name='species'),
    path('<slug:genus_slug>/<slug:species_slug>/strains/', 
        StrainListView.as_view(), name='strains'),
    path('<slug:genus_slug>/<slug:species_slug>/<slug:slug>/strain/', 
        StrainDetailView.as_view(), name='strain'),
    path('create_genus/', 
        CreateGenusView.as_view(), name='create_genus'),
    path('<slug:slug>/edit_genus/', 
        EditGenusView.as_view(), name='edit_genus'),
    path('<slug:slug>/delete_genus/', 
        DeleteGenusView.as_view(), name='delete_genus'),
    path('<slug:genus_slug>/create_species/', 
        CreateSpeciesView.as_view(), name='create_species'),
    path('<slug:genus_slug>/<slug:slug>/edit_species/', 
        EditSpeciesView.as_view(), name='edit_species'),
    path('<slug:genus_slug>/<slug:slug>/delete_species/', 
        DeleteSpeciesView.as_view(), name='delete_species'),
    path('<slug:genus_slug>/<slug:species_slug>/create_strain/', 
        CreateStrainView.as_view(), name='create_strain'),
    path('<slug:genus_slug>/<slug:species_slug>/<slug:slug>/edit_strain/', 
        EditStrainView.as_view(), name='edit_strain'),
    path('<slug:genus_slug>/<slug:species_slug>/<slug:slug>/delete_strain/', 
        DeleteStrainView.as_view(), name='delete_strain'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)