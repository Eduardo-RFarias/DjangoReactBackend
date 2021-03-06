from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, cpf, email, full_name, password=None):
        user = self.model(
            cpf=cpf,
            email=self.normalize_email(email),
            full_name=full_name,
        )
        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, cpf, email, full_name, password=None):
        user = self.model(
            cpf=cpf,
            email=self.normalize_email(email),
            full_name=full_name,
            is_superuser=True,
        )
        user.set_password(password)

        user.save()
        return user
