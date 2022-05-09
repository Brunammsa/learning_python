def consumo_do_carro(km, litro):
    calculo_km_l = km / litro
    if calculo_km_l < 8:
        return "Venda seu carro!"
    elif calculo_km_l > 8 and calculo_km_l < 14:
        return "Econômico!"
    elif calculo_km_l > 12:
        return "Super econômico!"

print(consumo_do_carro(5, 18))