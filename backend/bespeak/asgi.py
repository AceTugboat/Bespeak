"""
ASGI config for bespeak project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from pathlib import Path
from django.core.asgi import get_asgi_application


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bespeak.settings")

application = get_asgi_application()
