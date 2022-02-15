amigos = ["Aguiar", "Anna", "bruna", "Bruno", "Brenand", "Carol", "Camila", "Felipe", "Gleice", "Lucas", "Tenorio", "Thereza", "Vanessa"]

i = 0

while(i < len(amigos)):
   nome = amigos[i]
   if(len(nome) % 2 == 0):
      print(nome)
   i = i + 1