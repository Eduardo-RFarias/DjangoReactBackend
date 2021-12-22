from apps.User.models import User
from rest_framework.test import APITestCase


class BaseAuthenticatedTest(APITestCase):
    def login_and_set(self, cpf, password):
        self.get_user_or_create(cpf, password)

        loginResponse = self.login(cpf, password)

        user = loginResponse.data.get("user")
        token = loginResponse.data.get("token")

        self.set_token(token)

        return {"user": user, "token": token}

    def set_token(self, token):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

    def get_user_or_create(self, cpf, password):
        try:
            return User.objects.get(cpf=cpf)
        except User.DoesNotExist:
            return User.objects.create_superuser(
                cpf=cpf,
                email="email@example.com",
                full_name="example",
                password=password,
            )

    def login(self, cpf, password):
        return self.client.post("/auth/login/", {"cpf": cpf, "password": password})
