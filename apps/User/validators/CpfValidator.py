from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from validate_docbr import CPF


@deconstructible
class CpfValidator:
    def __init__(self):
        self.cpf_validator = CPF()

    def __call__(self, cpf):
        if not (self.is_cleared(cpf) and self.cpf_validator.validate(cpf)):
            raise ValidationError("Invalid Cpf, use only numbers.")

    def __eq__(self, other):
        return self.cpf_validator == other.cpf_validator

    def clear_cpf(self, cpf):
        return self.cpf_validator._only_digits(cpf)

    def is_cleared(self, cpf):
        return cpf.isnumeric()
