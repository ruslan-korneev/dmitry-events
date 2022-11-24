from typing import OrderedDict
from rest_framework import serializers
from apps.events.api.exceptions import CanBuyTicketOnlyOnce

from apps.events.models import Event, Prize, Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("id", "event", "owner")


class PrizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = ("id", "name", "description")


class EventSerializer(serializers.ModelSerializer):
    prize = PrizeSerializer(read_only=True)
    winner = TicketSerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            "id",
            "prize",
            "winner",
            "start",
            "finish",
            "link_to_stream",
            "amount_of_available_tickets",
        )
     

class TicketBuySerializer(TicketSerializer):
    event = EventSerializer(read_only=True)

    def validate(self, attrs: OrderedDict) -> OrderedDict:
        if self.context.get("event").tickets.filter(owner=attrs.get("owner")).exists():
            raise CanBuyTicketOnlyOnce
        return super().validate(attrs)
