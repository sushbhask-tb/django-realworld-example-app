from django.apps import AppConfig
from treebeardhq import Treebeard


class AuthenticationAppConfig(AppConfig):
    name = 'conduit.apps.authentication'
    label = 'authentication'
    verbose_name = 'Authentication'

    def ready(self):
        import conduit.apps.authentication.signals
        Treebeard.init(project_name="django-realworld-example-app", api_key="tb_prod_fM0LYUtStwMFhpYulLX8oKXZNul-r7O2vrwOR9wENXc")

# This is how we register our custom app config with Django. Django is smart
# enough to look for the `default_app_config` property of each registered app
# and use the correct app config based on that value.
default_app_config = 'conduit.apps.authentication.AuthenticationAppConfig'
