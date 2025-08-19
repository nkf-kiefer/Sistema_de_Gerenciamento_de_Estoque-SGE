from django.contrib import admin
from . import models


class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "serie_number",
    )  # campos do seu model que deve aparecer
    search_fields = ("title",)  # ordem que irá aparecer


admin.site.register(models.Product, ProductsAdmin)
