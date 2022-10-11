from django.apps import AppConfig


class VotingsysConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'votingsys'

    def ready(self):
        import votingsys.signals
