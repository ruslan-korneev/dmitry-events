from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from apps.events.models import Event


class IsWinner(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Event) -> bool:
        # instead of that we could confirm the number again
        return obj.winner == obj.winner
