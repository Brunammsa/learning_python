
def anagrama(string1, string2):
    resposta = False

    string1_ordenada = sorted(string1)
    string2_ordenada = sorted(string2)

    if string1_ordenada == string2_ordenada:
        resposta = True

    return resposta


print(anagrama("amor", "roma"))