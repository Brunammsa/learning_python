# Será sempre uma string quando estiver entre aspas "123", "abd", "432.34"
"""
Pode ser feita com:
aspas simples - 'abc'
aspas duplas - "abc"
aspas triplas - '''abc'''
"""
# aspas duplas triplas """abc"""

nome = "hello world"
print(nome)

# Para quebrar linhas em strings
name = "Angelina\nJolie"
print(name)

name2 = """Angelina
Jolie"""
print(name2)

# Para strings maiúsculas
maiusculo = "bruna melo"
print(maiusculo.upper())

# Para strings minúsculas
minusculo = "BRUNA MELO"
print(minusculo.lower())

# Transforma em uma lista de strings
teste = "Bruna Melo"
print(teste.split())

# Para selecionar uma posição na string, lembrando que sempre inicia-se no 0
teste2 = "Bruna Melo"
print(teste2[3])
print(teste[0:5])
print(teste2[5:])
print(teste2.split()[1])

# Começa do primeiro elemento até o último e inverte
print(teste2[::-1])

# Substitui a posição de lugar
print(teste2.replace("B", "M"))