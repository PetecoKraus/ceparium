# Generated by Django 3.2.8 on 2021-10-07 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211007_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genus',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='species',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='strain',
            name='access_number',
            field=models.CharField(max_length=10, unique=True, verbose_name='Ceparium Number'),
        ),
        migrations.AlterField(
            model_name='strain',
            name='strain_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Strain'),
        ),
    ]
