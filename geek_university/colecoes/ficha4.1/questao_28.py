vetor = []

while len(vetor) < 10:
    n = int(input('Digite um número >>> '))
    vetor.append(n)
print(vetor)

v1 = []
v2 = []
index = 0

for index in vetor:
    if index %2 == 0:
        v1.append(index)
    if index %2 != 0:
        v2.append(index)
    index += 1
print(v1)
print(v2)