import subprocess

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core import management


class Command(BaseCommand):
  """
  Reindex sphinx
  """
  def handle(self, *args, **kwargs):
      subprocess.call(['indexer', '--config', settings.SPHINX_CONFIG_FILE, '--all', '--rotate'])
