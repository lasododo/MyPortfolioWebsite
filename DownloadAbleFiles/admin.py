from django.contrib import admin
from .models import Program

Productx = Program


class ProgramAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    class Meta:
        model = Productx


admin.site.register(Productx, ProgramAdmin)