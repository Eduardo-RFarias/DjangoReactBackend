from apps.Todo.models import Todo
from apps.Todo.serializers import TodoSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models.UserModel import User
from ..serializers import UserSerializer


class UserView(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated]

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.get_queryset(), pk=pk)
        user.is_active = False
        user.save()

        return Response(self.get_serializer(user).data, status=status.HTTP_200_OK)

    @action(methods=["post"], detail=False)
    def create_superuser(self, request):
        body = request.POST.copy()
        body.pop("csrfmiddlewaretoken")

        serializer: UserSerializer = self.get_serializer(data=body)

        if serializer.is_valid(raise_exception=True):
            user = User.objects.create_superuser(**serializer.validated_data)
            return Response(self.get_serializer(user).data)

    @action(methods=["get"], detail=True)
    def get_todos(self, request, pk):
        todos = Todo.objects.filter(owner__pk=pk)
        serializer = TodoSerializer(todos, context={"request": request}, many=True)

        return Response(serializer.data)
