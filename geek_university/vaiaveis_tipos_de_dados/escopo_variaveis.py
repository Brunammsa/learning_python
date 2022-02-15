"""
Variáveis globais - são reconhecidas, seu escopo compreende todo o programa.
Variáveis locais - são reconhecidas apenas no bloco onde foram declaradas.

nome_da_variavel = valor_da_variavel

Pytho é uma linguagem dinâmica.
"""
# Exemplo de variavel global
nome = 28 # int # fora do escolpo
print(nome)
print(type(nome))

nome = "bruna melo" # agora string # fora do escolpo
print(nome)
print(type(nome))

# Exemplo de varivel local
numero = 28
novo = 0

if numero > 10:
    novo = numero + 10 # dentro do escolpo
    print(novo)
