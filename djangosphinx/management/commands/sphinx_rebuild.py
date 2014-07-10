from __future__ import  unicode_literals
import os, glob
import subprocess

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core import management


class Command(BaseCommand):
  """
  Generate new config file. Stop sphinx, reindex, then start sphinx
  """

  def handle(self, *args, **kwargs):
      self.generate_new_config()
      self.remove_spginx_data_files()
      self.stop_searchd()
      self.reindex()
      self.start_searchd()

  def remove_spginx_data_files(self):
      data_dir = settings.SPHINX_DATA_PATH
      binlog_dir = os.path.join(data_dir, 'binlog')

      for f in glob.glob(data_dir + '/*.*'):
        os.remove(f)

      for f in glob.glob(binlog_dir+ '/*.*'):
        os.remove(f)

  def generate_new_config(self):
      management.call_command('generate_sphinx_config', find_all=True)

  def stop_searchd(self):
      subprocess.call(['searchd', '--config', settings.SPHINX_CONFIG_FILE, '--stop'])

  def reindex(self):
      subprocess.call(['indexer', '--config', settings.SPHINX_CONFIG_FILE, '--all'])

  def start_searchd(self):
      subprocess.call(['searchd', '--config', settings.SPHINX_CONFIG_FILE])
