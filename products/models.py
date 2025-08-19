from django.db import models
from brands.models import Brand
from categories.models import Category


class Product(models.Model):
    title = models.CharField(blank=False, null=False, max_length=150)
    # não deixa deletar a marca se tiver produtos dela
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    description = models.TextField(blank=True, null=True)
    serie_number = models.CharField(max_length=200, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=20, decimal_places=2)
    selling_price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
