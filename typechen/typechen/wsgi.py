"""
WSGI config for typechen project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

profile = os.environ.get('TYPECHEN_PROFILE', 'develop')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typechen.settings.%s" % profile)

application = get_wsgi_application()
