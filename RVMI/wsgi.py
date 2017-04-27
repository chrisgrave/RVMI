"""
WSGI config for RVMI project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys

# add the RVMI project path into the sys.path
sys.path.append('/home/mzysscg3/django-RVMI/RVMI')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/home/mzysscg3/django-RVMI/DJANGO-RVMI/lib/python3.6/site-packages')

# poiting to the project settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RVMI.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

