from django.db.models.signals import post_save
from django.dispatch import receiver
from inflows.models import Inflow


# sempre que acontecer um post em inflow ele executa esse bloco
@receiver(post_save, sender=Inflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:  # se está dando entrada em um produto
        if instance.quantity > 0:
            product = instance.product
            product.quantity += instance.quantity  # fazendo o total que vai estar em estoque
            product.save()
