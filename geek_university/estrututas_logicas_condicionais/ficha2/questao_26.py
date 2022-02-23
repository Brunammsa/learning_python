distancia_km = int(input("Digite a distância em km: "))
litros_gasolina = int(input("Digite a quantidade de gasolina gasta: "))
calculo_kml =  distancia_km / litros_gasolina

if calculo_kml < 8:
    print("Venda seu carro!")
elif calculo_kml > 8 and calculo_kml < 14:
    print("Econômico!")
elif calculo_kml > 12:
    print("Super econômico!")
else:
    print("Valores inválidos, por favor, tente novamente")
