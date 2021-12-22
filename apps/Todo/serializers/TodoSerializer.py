from rest_framework import serializers

from ..models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = [
            "url",
            "id",
            "name",
            "description",
            "done",
            "created_at",
            "owner",
        ]
        read_only_fields = ["owner"]

    def create(self, validated_data):
        user = self.context["request"].user

        return Todo.objects.create(
            **validated_data,
            owner=user,
        )
