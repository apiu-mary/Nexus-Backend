from django.core.management.base import BaseCommand
from meter.models import Meter  # Import your Meter model

class Command(BaseCommand):
    help = 'Delete all records from the Meter model'

    def handle(self, *args, **options):
        # Delete all records from the Meter model
        Meter.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Successfully deleted all Meter records.'))
