from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from djgeojson.views import GeoJSONLayerView

from .views import *
from .models import Strain

app_name = 'core'

urlpatterns = [
    path('genuses/', GenusListView.as_view(), name='genuses'),
    path('<slug:genus_slug>/species/', SpeciesListView.as_view(), name='species'),
    path('<slug:genus_slug>/<slug:species_slug>/strains/', StrainListView.as_view(), name='strains'),
    path('<slug:genus_slug>/<slug:species_slug>/<slug:slug>/strain/', 
        StrainDetailView.as_view(), name='strain'),
    path('create_genus/', CreateGenusView.as_view(), name='create_genus'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)