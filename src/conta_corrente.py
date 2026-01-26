from __future__ import annotations
from conta import Conta
from cliente import Cliente
from historico import Historico

class ContaCorrente(Conta):
    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente, historico: Historico, limite: float, limite_saques: int):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = limite_saques
    
    @property
    def limite(self) -> float:
        return self._limite
    
    @limite.setter
    def limite(self, limite: float) -> None:
        self._limite = limite
    
    @property
    def limite_saques(self) -> int:
        return self._limite_saques
    
    @limite_saques.setter
    def limite_saques(self, limite_saques: int) -> None:
        self._limite_saques = limite_saques
