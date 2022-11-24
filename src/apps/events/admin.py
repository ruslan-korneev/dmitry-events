from django.contrib import admin

from src.apps.events.models import Event, Prize, Ticket


class HasWinnerFilter(admin.SimpleListFilter):
    title = "Event has winner"
    parameter_name = "has_winner"

    def lookups(self, request, model_admin) -> tuple:
        return ((True, True), (False, False))

    def queryset(self, request, queryset):
        return {
            None: queryset,
            "True": queryset.filter(winner__isnull=False),
            "False": queryset.filter(winner__isnull=True),
        }[self.value()]


class EventInline(admin.TabularInline):
    model = Event
    extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("__str__", "amount_of_available_tickets", "has_winner")
    list_filter = (HasWinnerFilter,)
    search_fields = ("name", "winner__owner")


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("event", "owner")
    search_fields = ("event", "owner")


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    inlines = (EventInline,)
    search_fields = ("name",)
