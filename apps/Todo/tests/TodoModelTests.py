from django.test import TestCase

from ..models import Todo
from django.utils import timezone


class TodoModelTests(TestCase):
    def test_create_todo(self):
        '''
        Testing the creation of a new Todo
        '''

        name = 'Test todo'
        description = 'This is an auto generated Todo'

        todo = Todo.objects.create(
            name=name,
            description=description
        )

        self.assertGreater(todo.id, 0)
        self.assertEqual(todo.name, name)
        self.assertEqual(todo.description, description)
        self.assertFalse(todo.done)
        self.assertLessEqual(todo.created_at, timezone.now())
