amigos = ["Aguiar", "Anna", "bruna", "Bruno", "Brenand", "Carol", "Camila", "Felipe", "Gleice", "Lucas", "Tenorio", "Thereza", "Vanessa"]

i = 0

while(i < len(amigos)):
   nome = amigos[i]
   if(nome[0].upper() == "B"):
      print(nome)
   i = i + 1