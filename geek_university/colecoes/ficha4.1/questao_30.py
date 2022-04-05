from random import randint

v1 = []
v2 = []

for numero in range(10):
    numb1 = randint(1, 10)
    v1.append(numb1)
    numb2 = randint(1, 10)
    v2.append(numb2)
v3 = set(v1).intersection(set(v2))

print(v1)
print(v2)
print(v3)
