from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from apps.events.api.views import EventViewSet


router = DefaultRouter()
router.register("events", EventViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('admin/', admin.site.urls),
]
