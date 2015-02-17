from __future__ import  unicode_literals

import subprocess
from django.conf import settings

def stop_searchd():
    subprocess.call(['searchd', '--config', settings.SPHINX_CONFIG_FILE, '--stop'])

def reindex():
    subprocess.call(['indexer', '--config', settings.SPHINX_CONFIG_FILE, '--all'])

def start_searchd():
    subprocess.call(['searchd', '--config', settings.SPHINX_CONFIG_FILE])

