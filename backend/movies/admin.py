from django.contrib import admin
from .models import Movie  # Importa el modelo Movie
# Register your models here.

admin.site.register(Movie)  # Regístralo para que aparezca en el admin
