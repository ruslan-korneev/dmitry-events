from django_filters import BooleanFilter, FilterSet

from src.apps.events.models import Event


class EventFilterSet(FilterSet):
    has_winner = BooleanFilter(method="filter_has_winner")

    class Meta:
        model = Event
        fields = ("has_winner",)

    def filter_has_winner(self, queryset, field, value):
        if field == "has_winner" and value is not None:
            queryset = queryset.exclude(winner__isnull=value)
        return queryset
