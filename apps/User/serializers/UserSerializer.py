from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="todo-detail",
    )

    class Meta:
        model = User
        fields = [
            "url",
            "cpf",
            "email",
            "full_name",
            "password",
            "is_active",
            "is_superuser",
            "last_login",
            "date_joined",
            "todos",
        ]
        read_only_fields = [
            "last_login",
            "is_superuser",
            "date_joined",
            "is_active",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def get_fields(self):
        fields = super().get_fields()

        request = self.context.get("request")

        if request:
            method = getattr(request, "method")

            if method == "PUT":
                fields["password"].required = False

        return fields
