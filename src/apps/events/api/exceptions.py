from rest_framework.exceptions import PermissionDenied


class CanBuyTicketOnlyOnce(PermissionDenied):
    default_detail = "You can buy ticket for this event only once with this number"
