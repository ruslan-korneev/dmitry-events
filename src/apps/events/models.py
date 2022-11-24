from django.db import models


class Ticket(models.Model):
    event = models.ForeignKey(
        "Event", on_delete=models.CASCADE, related_name="tickets"
    )
    owner = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.event} | {self.owner}"


class Event(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    # TODO: we could add list of winners and list of prize
    prize = models.ForeignKey("Prize", on_delete=models.SET_NULL, null=True, blank=True)
    winner = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField()
    finish = models.DateTimeField()
    link_to_stream = models.URLField(null=True, blank=True)
    image = models.URLField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(start__lt=models.F("finish")),
                name="correct_event_datetime",
            ),
        ]


    def __str__(self) -> str:
        return f"{self.name} | starts: {self.start} | finish {self.finish}"

    @property
    def amount_of_available_tickets(self) -> int:
        return self.tickets.filter(owner__isnull=True).count()

    @property
    def available_ticket(self) -> Ticket:
        return self.tickets.filter(owner__isnull=True).first()

    @property
    def has_winner(self) -> bool:
        return bool(self.winner)


class Prize(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
