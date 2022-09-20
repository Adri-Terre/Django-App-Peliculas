"""En este ejercicio tendrás que crear una aplicación en Django que almacene datos de directores de cine y luego
 se puedan ver sus películas, así como una descripción de las mismas.

Tienes que personalizar el admin de la aplicación y a su vez crear las vistas de cada una de las partes 
de la aplicación."""


from django.db import models

# Create your models here.
from django.urls import reverse
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Genero de la pelicula")

    def __str__(self):
        return self.name


class Pelicula(models.Model):
    title = models.CharField(max_length=32)
    director = models.ForeignKey("Director", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=100, help_text="Resumen de la pelicula")
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("pelicula_detail", args=[str(self.id)])


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_dead = models.DateField("Died", null=True, blank=True)

    def __str__(self):
        return "%s,%s" % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse("pelicula_detail", args=[str(self.id)])
