from django.core.management.base import BaseCommand
from inflows.models import Inflow
from django.db import connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Apagando todas as entradas...")
        Inflow.objects.all().delete()

        if connection.vendor == "sqlite":
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='inflows_inflow'")
            self.stdout.write("IDs resetados para começar a partir de 1 (SQLite).")
        else:
            self.stdout.write(
                self.style.WARNING("Reset de ID automático só implementado para SQLite.")
            )

        self.stdout.write(self.style.SUCCESS("entradas apagadas com sucesso."))
