from django.contrib import admin
from . import models


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )  # campos do seu model que deve aparecer
    search_fields = ("name",)  # ordem que irá aparecer


admin.site.register(models.Brand, BrandAdmin)
