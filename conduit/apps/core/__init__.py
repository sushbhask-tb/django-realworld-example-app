from django.apps import AppConfig
from treebeardhq import Treebeard


class CoreAppConfig(AppConfig):
    name = 'conduit.apps.core'
    label = 'core'
    verbose_name = 'Core'
    
    def ready(self):
        Treebeard.init(project_name="django-realworld-example-app", api_key="tb_prod_ckn7C2h0zk1AIAZ45ysO1ZtJgCGJatB4Jw9uXxYKHTM")


default_app_config = 'conduit.apps.core.CoreAppConfig'