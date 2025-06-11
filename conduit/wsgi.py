"""
WSGI config for conduit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from treebeardhq import Treebeard

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conduit.settings")

# Initialize Treebeard SDK
Treebeard.init(project_name="django-realworld-example-app")

application = get_wsgi_application()
