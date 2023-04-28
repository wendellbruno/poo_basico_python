class Caneta:
    def __init__(self, cor):

        self._cor_tinta = cor

    
    #nao chama como metodo, mas sim como atributo
    @property
    def cor(self):
        return self._cor_tinta
    
    @cor.setter
    def cor(self, valor):
        self._cor_tinta = valor

caneta = Caneta('Azul')
print(caneta.cor)
caneta.cor = 'Preta'
print(caneta.cor)