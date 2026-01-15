from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from transacao import Transacao
    from conta import Conta

class Cliente:

    def __init__(self, endereco: str, contas: list):
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(self, conta: "Conta", transacao: "Transacao"):
        pass
    
    def adicionar_conta(conta: "Conta"):
        pass
        
