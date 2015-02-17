from __future__ import  unicode_literals

from django.core.management.base import BaseCommand

from .commands import start_searchd


class Command(BaseCommand):
    """
    Start searchd
    """
    def handle(self, *args, **kwargs):
        start_searchd()
