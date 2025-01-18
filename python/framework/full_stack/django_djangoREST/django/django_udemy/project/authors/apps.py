from django.apps import AppConfig


class AuthorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authors'

    def ready(self, *args, **kwargs):
        #Esse import que liga os sinais com o profile.
        import authors.signals
        
        super_ready = super().ready(*args, **kwargs)

        return super_ready