from rest_framework import serializers
from ..models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
        extra_kwargs = {"owner": {"read_only": True}}

    def create(self, validated_data):
        user = self.context["request"].user

        return Todo.objects.create(
            **validated_data,
            owner=user,
        )
