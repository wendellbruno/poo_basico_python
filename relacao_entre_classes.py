class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None
    
    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, NomeFerramenta) -> None:
        self.NomeFerramenta = NomeFerramenta
    
    def escrever(self):
        return f'{self.NomeFerramenta} está escrevendo'

escritor = Escritor('Wendell')
caneta = FerramentaDeEscrever('Caneta Bic')

escritor.ferramenta = caneta
print(escritor.ferramenta.escrever())

