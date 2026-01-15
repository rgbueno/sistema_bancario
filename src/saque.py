from __future__ import annotations
from transacao import Transacao

class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor