# com find
def substring(agulha, palheiro):

    onde_esta = palheiro.find(agulha)
    return onde_esta


# sem find
def substring_na_mao(agulha, palheiro):

    if len(palheiro) < len(agulha):
        return -1

    primeira_posicao = None
    aux_da_agulha = ""
    agulha_indice = 0

    for palheiro_indice, _ in enumerate(palheiro):

        if aux_da_agulha == agulha:
            return primeira_posicao

        if agulha[agulha_indice] == palheiro[palheiro_indice]:
            aux_da_agulha += palheiro[palheiro_indice]
            agulha_indice += 1

            if primeira_posicao == None:
                primeira_posicao = palheiro_indice
        else:
            primeira_posicao = None
            agulha_indice = 0
            aux_da_agulha = ""
            
    return -1


str_teste = "breno bruno brenda brenand bruna bruno"

print(substring_na_mao("bruna", str_teste))
print(substring("bruna", str_teste))
