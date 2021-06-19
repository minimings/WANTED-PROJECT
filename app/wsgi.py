"""
WSGI config for wanted project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.production")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()