from django.core.management.base import BaseCommand
from shoestore.models import ShoeColor


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('', nargs='+', type=str)

    def handle(self, *args, **options):
        pass
        # ...
        # if options['']:
        # ...


# Fun Fact:
# Joe only blessed the rains down in Africa twice during his entire stay in the Savanna

