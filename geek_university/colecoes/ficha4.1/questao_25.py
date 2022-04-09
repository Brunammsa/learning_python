vetor = []
numero = 1

while len(vetor) < 100:
    numero_str = str(numero)
    ultima_posicao_numero_str = len(numero_str)-1
    if numero % 7 != 0 or numero_str[ultima_posicao_numero_str] == str(7):
        vetor.append(numero)
    numero += 1
print(vetor)
