from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from core.models import *

admin.site.register(Genus)
admin.site.register(Species)
admin.site.register(Strain, LeafletGeoAdmin)