"""
WSGI config for kronos_clock project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kronos_clock.settings")

application = get_wsgi_application()

try:
	from dj_static import Cling
	application = Cling(get_wsgi_application())
except:
	pass
#application = get_wsgi_application()
#application = DjangoWhiteNoise(application)