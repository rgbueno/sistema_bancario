from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, limite: float, limite_saques: int):
        self._limite = limite
        self._limite_saques = limite_saques
