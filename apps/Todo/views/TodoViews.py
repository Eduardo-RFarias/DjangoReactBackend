from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import Todo
from ..serializers import TodoSerializer


class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    permission_classes = [IsAuthenticated]
