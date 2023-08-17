import os

from django.core.management.base import BaseCommand
from django.core import management


class Command(BaseCommand):
    help = "Populate db with users and states"

    def handle(self, *args, **kwargs) -> str | None:
        self.stdout.write("\n - - - - ")
        self.stdout.write(self.style.HTTP_INFO("Importing fixtures"))

        self.stdout.write(self.style.HTTP_INFO("Importing users and states"))

        fixtures_dir = "registry/fixtures/"
        fixtures = sorted(os.listdir(fixtures_dir))
        print(fixtures)

        for fixture in fixtures:
            self.stdout.write(self.style.HTTP_INFO(f"Importing fixture: {fixture}"))
            management.call_command("loaddata", fixtures_dir+fixture)

            self.stdout.write(self.style.SUCCESS("\n Import was successful "))

