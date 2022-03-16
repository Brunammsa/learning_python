"""
Default Dict: Ao criar um dict utilizando-o,  nós informamos um valor default, podendo utilizar um lambda para isso. Este valor será utilizado sempre que
não houver um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor default dict será atribuído.

* Tudo visto em dict, vale para cá
"""
# Relembrando

meses = {'jan':1, 'fev': 2, 'mar':3}

print(meses) # aqui ele imprime o dict inteiro (chave:valor)
print(meses['fev']) # aqui ele irá imprimir apenas o valor correspondente

# Fazendo seu import

from collections import defaultdict

dicionario = defaultdict(lambda: 'valor adc')
dicionario['bruna'] = 'Melo'

print(dicionario)
print(dicionario['outro'])
print(dicionario)