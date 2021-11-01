from django.contrib import admin
from .models import Movie, Theater, Auditorium
# Register your models here.
from django.utils.html import format_html


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['id', 'image_tag', 'title']
    list_display_links = ['id', 'image_tag', 'title']
    list_per_page = 30

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50px;"/>'. format(obj.img))
    image_tag.short_description = 'Image'


@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name']


@admin.register(Auditorium)
class AuditoriumAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['idx', 'name', 'theater_num']
