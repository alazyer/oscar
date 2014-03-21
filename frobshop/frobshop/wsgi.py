"""
WSGI config for frobshop project.
"""

import os
import sys
import site

# adding the site-packages of the chosen virtualenv to work with
site.addsitedir('~/Github/virtualenvs/oscar/lib/python2.7/site-packages')

# adding the app's directory to the PYTHONPATH
sys.path.append('~/Github/oscar/frobshop')
sys.path.append('~/Github/oscar/frobshop/frobshop')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "frobshop.settings")

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
