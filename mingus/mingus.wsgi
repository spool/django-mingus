import site
from django.conf import settings
site.addsitedir('/home/django/domains/%s/%s/lib/python2.6/site-packages' % settings.DOMAIN_NAME)

import os
import sys

# put the Django project on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

os.environ["DJANGO_SETTINGS_MODULE"] = "mingus.settings"

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
