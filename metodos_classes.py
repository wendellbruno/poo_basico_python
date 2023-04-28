class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
     

     #apenas um metodo que nao tem acesso a classe nem atributos   
    @staticmethod
    def returnarNome(nome):
        return nome
    
    #decora um metodo factory
    @classmethod
    def criar_pessoa_padrao_anos(cls, nome):
        pessoa = cls(nome, 50)
        return pessoa
    
    

#a pessoa ja vem com o padrao de idade
p1 = Pessoa.criar_pessoa_padrao_anos(nome = 'Wendell')

print(vars(p1))
print(Pessoa.returnarNome('Wendell'))