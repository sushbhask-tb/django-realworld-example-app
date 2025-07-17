from django.apps import AppConfig
from lumberjack_sdk import Lumberjack


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'conduit.apps.core'
    
    def ready(self):
        Lumberjack.init(project_name="django-realworld-example-app", api_key="tb_prod_JKA0alwokXOsdyi1ZK3ZjqSKxlBkOopTFnkhuqmKslg")