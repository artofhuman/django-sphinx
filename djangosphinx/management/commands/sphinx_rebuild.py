from __future__ import  unicode_literals
import os, glob

from django.core.management.base import BaseCommand
from django.conf import settings
from django.core import management

from .commands import stop_searchd, reindex, start_searchd


class Command(BaseCommand):
    """
    Generate new config file. Stop sphinx, reindex, then start sphinx
    """

    def handle(self, *args, **kwargs):
        self.generate_new_config()
        self.remove_spginx_data_files()
        stop_searchd()
        reindex()
        start_searchd()

    def remove_spginx_data_files(self):
        data_dir = settings.SPHINX_DATA_PATH
        binlog_dir = os.path.join(data_dir, 'binlog')

        for f in glob.glob(data_dir + '/*.*'):
            os.remove(f)

        for f in glob.glob(binlog_dir+ '/*.*'):
            os.remove(f)

    def generate_new_config(self):
        management.call_command('generate_sphinx_config', find_all=True)

