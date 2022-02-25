"""
while espressão_boolena:
    //execução do loop

o bloco Do while será repetido enquanto a espressão booleana for verdadeira
"""
numero = 0
while numero < 10:
    print(numero)
    numero = numero + 1 #condição de repetição // CUIDADO COM O LOOP INFINITO !!!

# Do while:

resposta = " "

while resposta != "sim":
    resposta = input("Já acabou, Jéssica? ")