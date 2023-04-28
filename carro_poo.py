#self seria o this em outras linguagems, e se usa para pegar a instancia.
#sempre o primeiro parametro vai ser o self ( porém pode nomear como quiser)

class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def aceletar(self):
        print(f'{self.nome} está acelerando')



fusca = Carro(nome = 'Fusca')
celta = Carro(nome = 'Celta')
fiat =  Carro(nome = 'fiat')

fusca.aceletar()
celta.aceletar()
Carro.aceletar(fiat)