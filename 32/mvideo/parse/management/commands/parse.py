from django.core.management import BaseCommand

from parse.models import Comp
from parse.parsing import parse_comp


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-c', '--count', type=int,
                            help="Количество элементов для парсинга")

    def handle(self, *args, **options):
        count = options.get('count') or 0
        comps = parse_comp(count)
        Comp.objects.bulk_create(comps)