from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.events.models import Event, Ticket


@receiver(post_save, sender=Event)
def create_default_tickets(instance, created, **kwargs):
    if created:
        Ticket.objects.bulk_create([
            Ticket(event=instance)
            for _ in range(settings.AMOUNT_OF_TICKETS_FOR_EVENT)
        ])
