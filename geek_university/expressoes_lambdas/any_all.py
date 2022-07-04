"""
Any e All

all() retorna True se todos os elementos do iterável for verdadeiros ou ainda se o iterável está vazio.

any() retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retornará False
"""

# Exemplo all()

print(all([0, 1, 2, 3, 4])) # False porque o 0 é falso

print(all([1, 2, 3, 4])) # elementos True

print(all([])) # vazio retorna True

print(all("bruna")) # elementos True

nomes = ["bruna", "bruno", "breno", "brenand", "luquinhas"]

print(all([nome[0] == "b" for nome in nomes]))

print(all([num for num in [4, 2, 10, 8, 6] if num % 2 == 0]))

print(any([0, False, {}, []])) # 0 é False, False é False e vazio é False

print(any([0, 1, 2, 3])) # retornará True porquê ao menos algum é True

print(any([nome[0] == "l" for nome in nomes]))
