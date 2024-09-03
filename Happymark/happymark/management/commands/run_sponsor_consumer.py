# main_app/management/commands/run_sponsor_consumer.py
from django.core.management.base import BaseCommand
from rabbitmq import consume_sponsor # type: ignore

class Command(BaseCommand):
    help = 'Runs the sponsor consumer'

    def handle(self, *args, **options):
        consume_sponsor()