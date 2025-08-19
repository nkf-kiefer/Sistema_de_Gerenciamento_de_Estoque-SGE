from django.contrib import admin
from . import models


class InflowsAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "supplier",
        "quantity",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "supplier_name",
        "product_title",
    )


admin.site.register(models.Inflow, InflowsAdmin)
