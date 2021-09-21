from django.contrib import admin
from .models import Movie
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(Movie)
