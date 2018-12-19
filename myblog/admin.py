from django.contrib import admin
from .models import Product

Productx = Product


class ProductxAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = Productx


admin.site.register(Productx, ProductxAdmin)