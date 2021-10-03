from django.contrib import admin
from .models import Person
# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id']


admin.site.register(Person, PersonAdmin)
