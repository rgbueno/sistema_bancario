from conta import Conta
from transacao import Transacao

class Cliente:

    def __init__(self, endereco: str, contas: list):
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(conta: Conta, transacao: Transacao):
        pass
    
    def adicionar_conta(conta: Conta):
        pass
        
