# Ranges são utilizados para gerar sequências númericas específicas

"""
range(valor_de_início, valor_de_parada)
Caso não queira por valor de início, por apenas um valor, que será identificado como o de parada, iniciando-se no 0.
"""

# Opção 01
for i in range(11):
    print(i)

# Opção 02
for i in range(1,11):
    print(i)

# Opção 03
for i in range(1, 10, 2): # Aqui, o 2 significa alternando de 2 em 2
    print(i)

# Opção 4 (Inversa)

for i in range(10, 0, -1):
    print(i)