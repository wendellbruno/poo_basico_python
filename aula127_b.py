import json
from aula127_a import CAMINHO_ARQUIVO, Pessoa

with open(CAMINHO_ARQUIVO,'r') as arquivo:
    dados = json.load(arquivo)

    for index,pessoas in enumerate(dados):
         p = Pessoa(**pessoas)
         print(index, vars(p))