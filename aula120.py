class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa(nome='Wendell' , sobrenome='Bruno')
print(p1.nome)
#serve para editar a classe tbm, igual uma atribuição normal
print(p1.__dict__)
print(vars(p1))

dados = {'nome': 'Alaide', 'sobrenome': 'santos'}
p3 = Pessoa(**dados)
print(vars(p3))