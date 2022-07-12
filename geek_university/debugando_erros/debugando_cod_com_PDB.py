"""
Debugando com PDB: Python Debugger

- Para utilizar o Python Debugger, precisaremos* importar a biblioteca pdb e então utilizar a função set_trace()

* A partir do python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando do debug foi incorporado como
função bulti-in, funçaõ integrada, chamada breakpoint()

Comandos básicos para o pdb:

- l para listas onde estamos no código;
- n próxima linha;
- p imprime variável;
- c continua a execução, finalizando o debugger;
"""

# Exemplo 1 importando o pdb (não mais necessário)

nome = "bruna"
sobrenome = "melo"
import pdb; pdb.set_trace() # importando o pdb
nome_completo = nome + " " + sobrenome
quem_eh = "eu me chamo "
final = quem_eh + nome_completo
print(final)

""" invés de por o import pdb no início como fazemos com os outros importes, colocamos apenas onde pretendemos debuggar, 
e ao finalizar, já fazemos a remoção.
"""

# Exemplo 2 sem importar o pdb

nome = "bruna"
sobrenome = "melo"
breakpoint() # com função integrada
nome_completo = nome + " " + sobrenome
quem_eh = "eu me chamo "
final = quem_eh + nome_completo
print(final)
