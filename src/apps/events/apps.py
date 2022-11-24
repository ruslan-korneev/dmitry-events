from django.apps import AppConfig


class EventConfig(AppConfig):
    name = "apps.events"
    verbose_name = "Event"

    def ready(self):
        from apps.events import signals  # NOQA
