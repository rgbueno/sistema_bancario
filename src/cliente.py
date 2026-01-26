from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from transacao import Transacao
    from conta import Conta

class Cliente:

    def __init__(self, endereco: str, contas: list):
        self._endereco = endereco
        self._contas = contas
    
    @property
    def endereco(self) -> str:
        return self._endereco
    
    @endereco.setter
    def endereco(self, endereco: str) -> None:
        self._endereco = endereco
    
    @property
    def contas(self) -> list:
        return self._contas
    
    @contas.setter
    def contas(self, contas: list) -> None:
        self._contas = contas

    def realizar_transacao(self, conta: "Conta", transacao: "Transacao") -> None:
        pass
    
    def adicionar_conta(self, conta: "Conta") -> None:
        pass
        
