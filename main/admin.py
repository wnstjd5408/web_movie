from django.contrib import admin
from .models import Movie
# Register your models here.
from django.utils.html import format_html


class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['id', 'image_tag', 'title']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50px;"/>'. format(obj.img))
    image_tag.short_description = 'Image'


admin.site.register(Movie, MovieAdmin)
