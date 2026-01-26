from __future__ import annotations
from historico import Historico

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cliente import Cliente

class Conta:

    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente, historico: Historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    @property
    def saldo(self) -> float:
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo: float) -> None:
        self._saldo = saldo
    
    @property
    def numero(self) -> int:
        return self._numero
    
    @numero.setter
    def numero(self, numero: int) -> None -> None:
        self._numero = numero
    
    @property
    def agencia(self) -> str:
        return self._agencia
    
    @agencia.setter
    def agencia(self, agencia: str) -> None:
        self._agencia = agencia
    
    @property
    def cliente(self) -> "Cliente":
        return self._cliente
    
    @cliente.setter
    def cliente(self, cliente: "Cliente") -> None:
        self._cliente = cliente
    
    @property
    def historico(self) -> Historico:
        return self._historico
    
    @historico.setter
    def historico(self, historico: Historico) -> None:
        self._historico = historico

    def nova_conta(self, cliente: Cliente, numero: int) -> Conta:
        return None

    def sacar(self, valor: float) -> bool:
        return True

    def depositar(self, valor: float) -> bool:
        return True
