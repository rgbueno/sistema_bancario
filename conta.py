from cliente import Cliente
from conta import Conta
from historico import Historico

class Conta:

    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente, historico: Historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    def saldo(self) -> float:
        return None

    def nova_conta(self, cliente: Cliente, numero: int) -> Conta:
        return None

    def sacar(self, valor: float) -> bool:
        return True

    def depositar(self, valor: float) -> bool:
        return True
