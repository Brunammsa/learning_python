#adc elemento a lista

lista1 = ["bruno", "breno", "brennand"]

lista1.append("jorginho")

#obs1> pode criar uma vazia e ir adc as poucos

#procurando elemento dentro da lista
if "jorginho" in lista1: 
    print("jorginho esta na lista")

#deletando elemento na lista

del lista1[2:] #: quer dizer até o final
print(lista1)

#obs:1 p remover todo mundo [:]

#ordenando lista

lista2 = [50, 25, 64, 5, 3, 19, 0]

lista2.sort() 
print(lista2)

#obs1:ordena do maior para o menor utiliza-se .sort(reverse=true) e do menor para o maior .sort() vazio
#obs2: para reverter a ordem, sem ordenar .reverse()
#obs2: .sort e (reverse=true) ordena strings em ordem alfabetica tambem

