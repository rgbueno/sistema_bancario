from datetime import date
from cliente import Cliente

class PessoaFisica(Cliente):

    def __init__(self, cpf: str, nome: str, data_nascimento: date):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento


