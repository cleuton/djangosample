from django.contrib import admin

# Register your models here.

from .models import Recado, Seguidor

admin.site.register(Recado)
admin.site.register(Seguidor)