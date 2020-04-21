from django.core.management import BaseCommand

from parse.models import Comp
from parse.parsing import parse_comp


class Command(BaseCommand):

    def handle(self, *args, **options):
        comps = parse_comp()
        Comp.objects.bulk_create(comps)