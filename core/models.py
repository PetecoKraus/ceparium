from django.db import models
from django.db.models.deletion import CASCADE
from autoslug import AutoSlugField

from datetime import datetime
from django.contrib.gis.db import models as gismodels
from django.db.models import Manager as GeoManager
from django.db.models.fields import BLANK_CHOICE_DASH

class Genus(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', unique=True)
    slug = AutoSlugField(null=True, default=None, populate_from='name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genus'
        verbose_name_plural = 'Genuses'
        db_table = 'genus'
        ordering = ['name']


class Species(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', unique=True)
    genus = models.ForeignKey(Genus, on_delete=CASCADE)
    slug = AutoSlugField(null=True, default=None, populate_from='name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Species'
        verbose_name_plural = 'Species'
        db_table = 'species'
        ordering = ['name']


class Strain(models.Model):
    species = models.ForeignKey(Species, on_delete=CASCADE)
    strain_name = models.CharField(max_length=50, verbose_name='Strain', unique=True)
    access_number = models.CharField(max_length=50, verbose_name='Ceparium Number', unique=True)
    taxon_rank = models.CharField(null=True, blank=True, max_length=50, verbose_name=('Taxonomic Rank'))
    collection_date = models.DateField(default=datetime.now, verbose_name='Collection Date')
    reactivation_date = models.DateField(verbose_name='Reactivation Date')
    preparation = models.TextField(null=True, blank=True, verbose_name='Preparation')
    photo = models.ImageField(upload_to = 'core/static/ceparium/images/strains/', 
                             default = 'core/static/ceparium/images/no-img.jpg',
                             blank=True)
    collection_place = models.CharField(max_length=50,verbose_name='Collection Place')
    collection_point = gismodels.PointField(null=True, blank=True)
    isolated_by = models.CharField(null=True, blank=True, max_length=50, verbose_name='Isolated by')
    identified_by = models.CharField(null=True, blank=True, max_length=50, verbose_name='Identified by')

    def __str__(self):
        return self.strain_name

    class Meta:
        verbose_name = 'Strain'
        verbose_name_plural = 'Strains'
        db_table = 'strain'
        ordering = ['strain_name']