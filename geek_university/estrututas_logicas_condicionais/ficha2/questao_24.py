valor_produto = float(input("Digite o valor do produto: R$ "))
destino_estado = input("Digite o destino final do produto: ")

taxa_mg = valor_produto / 0.93
taxa_sp = valor_produto / 0.88
taxa_rj = valor_produto / 0.85
taxa_ms = valor_produto / 0.92

if destino_estado == "Minas Gerais":
    print("O valor final do produto para o estado {} já com a taxa de 7 porcento é de {}".format(destino_estado, round(taxa_mg, 2)))
elif destino_estado == "São Paulo":
    print("O valor final do produto para o estado {} já com a taxa de 12 porcento é de {}".format(destino_estado, round(taxa_sp, 2)))
elif destino_estado == "Rio de Janeiro":
    print("O valor final do produto para o estado {} já com a taxa de 7 porcento é de {}".format(destino_estado, round(taxa_rj, 2)))
elif destino_estado == "Mato Grosso do Sul":
    print("O valor final do produto para o estado {} já com a taxa de 7 porcento é de {}".format(destino_estado, round(taxa_ms, 2)))
else:
    print("Estado inválido, favor, tente outro")



