import contas
import pessoa

class Banco:

    def __init__(
            self,
            agencias: list[int] | None = None,
            clientes: list[pessoa.Pessoas] | None = None,
            contas: list[contas.Conta] | None = None
            ) -> None:
        
            self.agencias = agencias or []
            self.clientes = clientes or []
            self.contas = contas or []
        

    def _chega_agencia(self, agencia):
          if agencia.agencias in self.agencias:
                return True
          return False
    
    def _chega_cliente(self, cliente):
          if cliente.clientes in self.clientes:
                return True
          return False
    
    def _chega_conta(self, conta):
          if conta.contas in self.contas:
                return True 
          return False


    def autenticar(self, cliente: pessoa.Pessoas, conta: contas.Conta): 
        return self._chega_agencia(conta) and \
               self._chega_cliente(cliente) and \
               self._chega_agencia(conta)
    

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == "__main__":

    cliente = pessoa.Cliente('Wendell', 27)
    cliente.conta = contas.ContaCorrente(120,100,0,0) # type: ignore
    banco = Banco()
    banco.clientes.extend([cliente])
    banco.contas.extend([cliente.conta])
    print(banco)