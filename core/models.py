from django.db import models
from datetime import datetime
from django.db.models.deletion import CASCADE
from djgeojson import fields

class Genus(models.Model):
    name = models.CharField(max_length=20, verbose_name='Name', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genus'
        verbose_name_plural = 'Genuses'
        db_table = 'genus'
        ordering = ['name']


class Species(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name', unique=True)
    genus = models.ForeignKey(Genus, on_delete=CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Species'
        verbose_name_plural = 'Species'
        db_table = 'species'
        ordering = ['genus']


class Strain(models.Model):
    species = models.ForeignKey(Species, on_delete=CASCADE)
    strain_name = models.CharField(max_length=20, verbose_name='Strain', unique=True)
    access_number = models.CharField(max_length=10, verbose_name='Ceparium Number', unique=True)
    collection_date = models.DateField(default=datetime.now, verbose_name='Collection Date')
    reactivation_date = models.DateField(verbose_name='Reactivation Date')
    collection_place = models.CharField(max_length=50,verbose_name='Collection Place')
    collection_point = fields.PointField(null=True, blank=True)

    def __str__(self):
        return self.strain_name

    class Meta:
        verbose_name = 'Strain'
        verbose_name_plural = 'Strains'
        db_table = 'strain'
        ordering = ['species']