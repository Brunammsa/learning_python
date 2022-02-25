# Utilizamos o break para sair de loops de maneira projetada

# Exemplo com for:

for numero in range(1, 10):
    if numero == 6:
        break
    else:
        print(numero)
print("Sai do loop")

# Exemplo com while

while True: # Enquanto for verdadeiro
    comando = input("Digite sair para sair: ")
    if comando == "sair":
        break