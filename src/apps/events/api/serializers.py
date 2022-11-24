from rest_framework import serializers

from apps.events.models import Event, Prize, Ticket


class PrizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = ("id", "name", "description")


class EventSerializer(serializers.ModelSerializer):
    prize = PrizeSerializer(read_only=True)

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
     

class CurrentEventDefault(serializers.CurrentUserDefault):
    def __call__(self, serializer_field):
        return serializer_field.context["event"]


class TicketBuySerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = ("id", "event", "owner")
