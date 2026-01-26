from datetime import date
from cliente import Cliente

class PessoaFisica(Cliente):

    def __init__(self, endereco:str , contas: list, cpf: str, nome: str, data_nascimento: date):
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento


    @property
    def cpf(self) -> str:
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf: str) -> None:
        self._cpf = cpf
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome
    
    @property
    def data_nascimento(self) -> date:
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date) -> None:
        self._data_nascimento = data_nascimento    
