from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from apps.base.api.mixins import PermissionPerActionMixin, SerializerPerActionMixin
from apps.events.api.paginators import EventPaginator
from apps.events.api.permissions import IsWinner
from apps.events.api.serializers import EventSerializer, PrizeSerializer, TicketBuySerializer
from apps.events.models import Event, Ticket


class EventViewSet(
    SerializerPerActionMixin,
    PermissionPerActionMixin,
    ListModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    action_serializers = {
        "default": EventSerializer,
        "buy_ticket": TicketBuySerializer,
        "get_prize": PrizeSerializer,
    }
    action_permissions = {
        "default": [AllowAny],
        "get_prize": [IsWinner],
    }
    pagination_class = EventPaginator
    queryset = Event.objects.all()
    # TODO: permission_classes

    @action(detail=True, methods=["POST"])
    def buy_ticket(self, request: Request, *args, **kwargs):
        event = self.get_object()
        try:
            ticket = event.available_ticket
        except Ticket.DoesNotExist:
            return Response(
                {"detail": "No available tickets"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(
            instance=ticket, data=request.data, context={"event": self.get_object(), "request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["GET"])
    def get_prize(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(instance=self.get_object().prize)
        return Response(serializer.data, status=status.HTTP_200_OK)
