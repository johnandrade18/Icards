from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from usuarios.models import Usuario

@admin.register(Usuario)
class UserAdmin(BaseUserAdmin):
    pass
