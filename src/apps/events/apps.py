from django.apps import AppConfig


class EventConfig(AppConfig):
    name = "src.apps.events"
    verbose_name = "Event"

    def ready(self):
        from src.apps.events import signals  # NOQA
