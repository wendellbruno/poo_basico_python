from abc import ABC, abstractmethod

class Conta(ABC):
    
    def __init__(self, agencia: int, conta: int, saldo: float= 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor) -> float: ...

    def detalhes(self, msg: str='') -> None:
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('----')

    def depositar(self, valor) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPOSITO {valor})')
        return self.saldo
    


class ContaPoupanca(Conta):

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
    
        print('NÃO FOI POSSIVEL SACAR O VALOR DESEJADO')
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self.saldo

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.conta!r}, {self.agencia!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaCorrente(Conta):

    def __init__(self, agencia: int, conta: int, saldo: float= 0,limite: float = 100) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite


    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite


        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
    
        print('NÃO FOI POSSIVEL SACAR O VALOR DESEJADO')
        print(f'SEU LIMITE É {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self.saldo
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.conta!r}, {self.agencia!r}, {self.saldo!r}, {self.limite})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    cp1 = ContaPoupanca(111,222)

    """ cp1.sacar(1)
    cp1.depositar(100)
    cp1.sacar(50)
    cp1.detalhes()
    print('####') """

    cc = ContaCorrente(111,222)
    cc.sacar(1)
    cc.depositar(100)
    cc.sacar(50)
    cc.sacar(50)
    cc.sacar(50)
    cc.sacar(50)


    cc.detalhes()
    print('####')