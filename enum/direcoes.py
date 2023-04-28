import enum

class Direcoes(enum.Enum):
    ESQUERDA = 1
    DIREITA = 2
    LADO = 'lado'


print(Direcoes(1))
print(Direcoes('lado'))
print(Direcoes(1). name, Direcoes.ESQUERDA.value)
