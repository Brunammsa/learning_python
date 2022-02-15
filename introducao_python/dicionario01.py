# DICIONARIO = {"CHAVE": "VALOR"} uma chave e um valor correspondente.

dicio_qualidades1 = {"Bruno": "bom professor"}
print(dicio_qualidades1["Bruno"])

dicio_qualidades2 = {"Bruna": "boa amiga", "Vanessa": "gosta de reclamar"}

for chave in dicio_qualidades2:
    print(dicio_qualidades2[chave])

#obs1: primeiro exemplo conjunto com apenas um elemebro relacionado na chave, segundo exemplo vários elementos relacionados dentro da chave.

dicio_qualidades3 = {"A":"a de amor", "B":"b de baixinho", "C":"c de coração"}

print(dicio_qualidades3["B"])

#obs2: para localizar um valor dentro da chave, utiliza-se a chave correspondente, diferente da lista, que é por ordem de 0 a...

print(dicio_qualidades3)

#obs3: para imprimir todas as chaves, basta por a variavel

for chave in dicio_qualidades3:
    print(chave)
#obs4: para imprimir apenas as chaves
    print(dicio_qualidades3[chave])
#obs5: para imprimir as chaves com os valores
    print(chave + ":" + dicio_qualidades3[chave])
#obs6: imprimi chave+valor

for i in dicio_qualidades2.items():
    print(i)
#obs7: utilizando o metodo items() conseguimos imprimir uma tupla (perguntar a bruno melhor sobre isso), como se fosse uma lista, só que separadamente, chave com valor.

for i in dicio_qualidades3.values():
    print(i)
#obs8: imprimi só os valores (perguntar p bruno pq ta imrprimindo na ordem invertida)
#obs9: se quiser navegar pelas chaves, troca o .values() por .keys()
