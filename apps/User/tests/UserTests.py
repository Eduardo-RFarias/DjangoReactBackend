from django.contrib.auth.hashers import check_password
from rest_framework import status

from ..models import User
from . import BaseAuthenticatedTest

cpf = "03699132137"
password = "123456"


class UserTests(BaseAuthenticatedTest):
    def test_user_model(self):
        email = "eduardo@example.com"
        full_name = "Eduardo Rodrigues"

        user = User.objects.create_user(
            cpf=cpf,
            email=email,
            full_name=full_name,
            password=password,
        )

        self.assertEqual(user.cpf, cpf)
        self.assertEqual(user.email, email)
        self.assertEqual(user.full_name, full_name)
        self.assertTrue(check_password(password, user.password))

        user.delete()

        superuser = User.objects.create_superuser(
            cpf=cpf,
            email=email,
            full_name=full_name,
            password=password,
        )

        self.assertEqual(superuser.cpf, cpf)
        self.assertEqual(superuser.email, email)
        self.assertEqual(superuser.full_name, full_name)
        self.assertTrue(check_password(password, superuser.password))

        superuser.delete()

    def test_user_list(self):
        self.login_and_set(cpf, password)

        response = self.client.get("/api/user/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data[0].get("url"))

    def test_user_detail(self):
        self.login_and_set(cpf, password)

        response = self.client.get(f"/api/user/{cpf}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data.get("url"))

    def test_user_create(self):
        self.login_and_set(cpf, password)

        new_cpf = "83607625115"

        response = self.client.post(
            "/api/user/",
            {
                "cpf": new_cpf,
                "email": "email@example.com",
                "full_name": "user example",
                "password": password,
            },
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data.get("url"))
        self.assertTrue(response.data.get("cpf"), new_cpf)

    def test_user_update(self):
        new_name = "Teste de edição"

        login_response = self.login_and_set(cpf, password)

        user = login_response.get("user")
        user["full_name"] = new_name

        response = self.client.put(f"/api/user/{cpf}/", user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("full_name"), new_name)

    def test_user_delete(self):
        self.login_and_set(cpf, password)

        response = self.client.delete(f"/api/user/{cpf}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data.get("is_active"))
