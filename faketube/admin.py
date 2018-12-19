from django.contrib import admin
from .models import VideoUpload

Productx = VideoUpload


class ProgramAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    class Meta:
        model = Productx


admin.site.register(Productx, ProgramAdmin)
