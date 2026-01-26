from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from conta import Conta

class Transacao:
    def __init__(self):
        self._timestamp: str = ""
    
    @property
    def timestamp(self) -> str:
        return self._timestamp
    
    @timestamp.setter
    def timestamp(self, timestamp: str) -> None:
        self._timestamp = timestamp

    def registrar(self, conta: "Conta") -> None:
        pass
    