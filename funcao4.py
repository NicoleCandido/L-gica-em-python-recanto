def e_par(num):
    return num % 2 == 0

numeros = [12, 23, 36, 45, 58, 67, 78]

for num in numeros:
    if e_par(num):
        print(num, "é par")
    else:
        print(num, "é impar")