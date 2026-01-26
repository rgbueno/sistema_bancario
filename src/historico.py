from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from transacao import Transacao

class Historico:
    def __init__(self):
        self._transacoes: list["Transacao"] = []
    
    @property
    def transacoes(self) -> list["Transacao"]:
        return self._transacoes
    
    @transacoes.setter
    def transacoes(self, transacoes: list["Transacao"]) -> None:
        self._transacoes = transacoes

    def adicionar_transacao(self, transacao: "Transacao") -> None:
        self._transacoes.append(transacao)