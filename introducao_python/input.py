x = int(input("digite um numero inteiro para calcular o fat: "))
fatorial = 1

for i in range(0, x + 1):
    fatorial = fatorial * i
print("fatorial de " + str(x) + " eh " + str(fatorial))