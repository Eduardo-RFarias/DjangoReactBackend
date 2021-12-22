from apps.User.models import User
from django.shortcuts import get_object_or_404
from django.test import RequestFactory
from django.utils import timezone
from rest_framework import status

from ..models import Todo
from ..serializers import TodoSerializer
from .BaseAuthenticatedTest import BaseAuthenticatedTest

name = "Test todo"
description = "This is an auto generated Todo"


class TodoModelTests(BaseAuthenticatedTest):
    def setUp(self) -> None:
        loginResponse = self.login_and_set("03699132137", "123456")
        self.userJson = loginResponse.get("user")
        self.user = User.objects.get(cpf=self.userJson.get("cpf"))

    def test_todo_model(self):
        todo = Todo.objects.create(name=name, description=description)

        self.assertGreater(todo.id, 0)
        self.assertEqual(todo.name, name)
        self.assertEqual(todo.description, description)
        self.assertFalse(todo.done)
        self.assertLessEqual(todo.created_at, timezone.now())
        self.assertIsNone(todo.owner)

        todo.delete()

    def test_todo_list(self):
        todo = Todo.objects.create(name=name, description=description, owner=self.user)

        request = RequestFactory().post("/")
        todoJson = TodoSerializer(todo, context={"request": request}).data

        response = self.client.get("/api/todo/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data[0].get("name"),
            todoJson.get("name"),
        )
        self.assertEqual(
            response.data[0].get("description"),
            todoJson.get("description"),
        )
        self.assertEqual(
            response.data[0].get("owner"),
            todoJson.get("owner"),
        )

    def test_todo_detail(self):
        todo = Todo.objects.create(name=name, description=description, owner=self.user)

        request = RequestFactory().post("/")
        todoJson = TodoSerializer(todo, context={"request": request}).data

        response = self.client.get(f"/api/todo/{todo.pk}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data.get("name"),
            todoJson.get("name"),
        )
        self.assertEqual(
            response.data.get("description"),
            todoJson.get("description"),
        )
        self.assertEqual(
            response.data.get("owner"),
            todoJson.get("owner"),
        )

    def test_todo_create(self):
        response = self.client.post(
            "/api/todo/",
            {"name": name, "description": description},
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("name"), name)
        self.assertEqual(response.data.get("description"), description)
        self.assertEqual(response.data.get("owner"), self.userJson.get("url"))

    def test_todo_update(self):
        todo = Todo.objects.create(name=name, description=description, owner=self.user)

        request = RequestFactory().post("/")
        todoJson = TodoSerializer(todo, context={"request": request}).data

        new_description = "Updated description for testing"
        todoJson["description"] = new_description

        response = self.client.put(f"/api/todo/{todo.pk}/", todoJson)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("description"), new_description)

    def test_todo_delete(self):
        todo = Todo.objects.create(name=name, description=description, owner=self.user)

        response = self.client.delete(f"/api/todo/{todo.pk}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Todo.DoesNotExist):
            Todo.objects.get(pk=1)
