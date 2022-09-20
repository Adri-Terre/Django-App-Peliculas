from django.contrib import admin

# Register your models here.
from .models import Genre, Director, Pelicula

admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Pelicula)
