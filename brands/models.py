from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # cria somente uma vez
    updated_at = models.DateTimeField(auto_now=True)  # cria sempre que atualizado

    class Meta:  # criando uma ordenação por ordem alfabética de acordo nome
        ordering = ["name"]

    def __str__(self):  # para que retorne o nome e não o id
        return self.name
