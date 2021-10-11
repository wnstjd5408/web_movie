from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
# Register your
from . import models


class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'gender', 'age',
                    'phone_number', 'address', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ('Personal info', {"fields": ('name',
                                      'gender', 'age', 'phone_number', 'address',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'gender', 'age', 'phone_number', 'address' 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
