from django.core.management.base import BaseCommand, CommandError
from seguros.models import (
    AutoList,
    MotoList,
    CamionList
)
from django.conf import settings


class Command(BaseCommand):
    help = "Load Excel Data into the database"

    def handle(self, *args, **options):
        try:
            self.stdout.write("Loading Excel Data")
            import json

            files = [
                ("Autos", AutoList),
                ("Camion", MotoList),
                ("Moto", CamionList),
            ]

            for f in files:
                data = []
                with open(settings.BASE_DIR / (f[0] + ".json"), "r") as rf:
                    data.extend(json.load(rf))
                    for row in data:
                        instance = f[1](**row)
                        instance.save()

        except Exception as err:
            self.stdout.write(err)