from rest_framework.serializers import ValidationError
from validate_docbr import CPF


class CpfValidator:
    def __init__(self, cpf):
        self.cpf_validator = CPF()
        self.cpf = self.cpf_validator._only_digits(cpf)

    def __call__(self):
        if not self.cpf_validator.validate(self.cpf):
            raise ValidationError("Invalid Cpf")

        return self.cpf
