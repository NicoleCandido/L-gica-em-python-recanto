matriz = [
    [10,30,50],
    [40,76,89],
    [55,37,23]
]

for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            print(valor, "é par")
        else:
            print(valor, "é impar")