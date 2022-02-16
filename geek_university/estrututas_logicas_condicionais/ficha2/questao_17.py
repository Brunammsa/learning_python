base_maior = int(input("Digite o valor da base maior do trapesio: ")) # Fiquei na dúvida se pode ter float em trapézio
base_menor = int(input("Digite o valor do lado menor do trapezio: "))
altura = int(input("Digite o valor da altura do trapezio: "))

area_trapezio = (base_maior+base_menor) * altura / 2

if area_trapezio > 0:
    print("A área do trapézio é {}".format(area_trapezio))

# Não sei se a questão só pediu isso