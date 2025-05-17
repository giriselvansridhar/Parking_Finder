import csv
from django.core.management.base import BaseCommand
from Authentication.models import Landlord
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Import landlords from CSV file'

    def handle(self, *args, **kwargs):
        filepath = os.path.join(settings.BASE_DIR, 'Authentication', 'data', 'landlords.csv')

        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            landlords = []
            for row in reader:
                landlords.append(Landlord(
                    name=row['name'],
                    email=row['email'],
                    phone=row['phone'],
                    pincode=row['pincode'],
                    address=row['address'],
                    area=row['area'],
                    landmark=row['landmark'],
                    city=row['city'],
                    state=row['state'],
                    country=row['country'],
                    pin=row['pin'],
                    latitude=row['latitude'],
                    longitude=row['longitude'],
                ))

            Landlord.objects.bulk_create(landlords)
            self.stdout.write(self.style.SUCCESS(f'Successfully imported {len(landlords)} landlords.'))
