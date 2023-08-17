import random

from django.core.management.base import BaseCommand

from registry.models import People, State


class Command(BaseCommand):
    help = "Populate database with 200 random people"


    def handle(self, *args, **options):
        states = State.objects.all()

        # for _ in range(200): 