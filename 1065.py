contador = 0
for _ in range(5):
    valor = int(input())
    if valor % 2 == 0:
        contador += 1
print(f"{contador} valores pares")
