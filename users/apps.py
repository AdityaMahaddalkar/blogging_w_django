from django.apps import AppConfig
from django.views.decorators.csrf import csrf_exempt

class UsersConfig(AppConfig):
    name = 'users'

    @csrf_exempt
    def ready(self):
        import users.signals
