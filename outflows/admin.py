from django.contrib import admin
from . import models


class OutflowsAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "quantity",
        "created_at",
        "updated_at",
    )
    search_fields = ("product__title",)


admin.site.register(models.Outflow, OutflowsAdmin)
