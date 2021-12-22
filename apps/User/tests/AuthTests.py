from django.test import RequestFactory
from rest_framework import status

from ..serializers import UserSerializer
from . import BaseAuthenticatedTest

cpf = "03699132137"
password = "123456"


class AuthTests(BaseAuthenticatedTest):
    def test_login_view(self):
        user = self.get_user_or_create(cpf, password)

        request = RequestFactory().post("/")
        userJson = UserSerializer(user, context={"request": request}).data

        response = self.login(cpf, password)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIsNotNone(response.data.get("expiry"))
        self.assertIsNotNone(response.data.get("token"))
        self.assertIsNotNone(response.data.get("user"))

        authenticated_user = response.data.get("user")

        self.assertEqual(authenticated_user.get("url"), userJson.get("url"))
        self.assertEqual(authenticated_user.get("cpf"), userJson.get("cpf"))

    def test_logout_view(self):
        self.login_and_set(cpf, password)

        response = self.client.post("/auth/logout/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        unauthorized_response = self.client.get("/api/user/")

        self.assertEqual(
            unauthorized_response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )

    def test_user_view_authentication(self):
        response = self.client.get("/api/user/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
