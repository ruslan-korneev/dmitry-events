class SerializerPerActionMixin:
    action_serializers: dict = {}
    serializer_class = None
    action: str = ""

    def get_serializer_class(self):
        assert (
            self.action_serializers
        ), f"{self.__class__.__name__} needs to define a `action_serializers` attribute"
        assert self.action_serializers.get(
            "default"
        ), f"{self.__class__.__name__} needs to define `default` in `action_serializers` attribute"
        self.serializer_class = self.action_serializers.get(
            self.action, self.action_serializers["default"]
        )

        return super(SerializerPerActionMixin, self).get_serializer_class()


class PermissionPerActionMixin:
    action_permissions: dict = {}
    permission_classes: list = []
    action: str = ""

    def get_permissions(self):
        assert (
            self.action_permissions
        ), f"{self.__class__.__name__} needs to define a `action_permissions` attribute"
        assert self.action_permissions.get(
            "default"
        ), f"{self.__class__.__name__} needs to define a `default` in 'action_permissions' attribute"
        self.permission_classes = self.action_permissions.get(
            self.action, self.action_permissions["default"]
        )

        return super(PermissionPerActionMixin, self).get_permissions()
