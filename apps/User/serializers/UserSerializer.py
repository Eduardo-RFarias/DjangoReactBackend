from rest_framework import serializers

from ..models import User
from ..validators import CpfValidator


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="user-detail",
        read_only=True,
    )
    todos = serializers.HyperlinkedIdentityField(
        view_name="user-get-todos",
        read_only=True,
    )
    cpf = serializers.CharField(
        validators=[CpfValidator],
        read_only=True,
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = [
            "last_login",
            "is_superuser",
            "is_staff",
            "date_joined",
            "groups",
            "user_permissions",
            "is_active",
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def get_fields(self):
        fields = super().get_fields()

        request = self.context.get("request")

        if request:
            method = getattr(request, "method")

            if method == "PUT":
                fields["password"].required = False
            elif method == "POST":
                fields["cpf"].read_only = False

        return fields
