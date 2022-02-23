altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

if altura <= 1.20 and peso <= 60:
    print("Classificação A")
elif altura <= 1.20 and peso >= 60 and peso <= 90:
    print("Classificação D")
elif altura <= 1.20 and peso > 90:
    print("Classificação G")
elif altura >= 1.20 and altura <= 1.70 and peso <= 60:
    print("Classificação B")
elif altura >= 1.20 and altura <= 1.70 and peso >= 60 and peso <= 90:
    print("Classificação E")
elif altura >= 1.20 and altura <= 1.70 and peso > 90:
    print("Classificação H")
elif altura > 1.70 and peso <= 60:
    print("Classificação C")
elif altura > 1.70 and peso >= 60 and peso <= 90:
   print("Classificação F")
elif altura > 1.70 and peso > 90:
    print("Classificação I")
else:
    print("valores de altura ou de peso indisponíveis, por favor, tente novamente")
