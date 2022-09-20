from django.shortcuts import render

from cineapp.models import Director, Pelicula

# Create your views here.

# from .models import Pelicula,Director


def index(request):
    num_peliculas = Pelicula.objects.all().count()
    num_directores = Director.objects.all().count()

    return render(request, "index.html", context={"num_peliculas", "num_directores"})
