#faça um programa que tenha como variável "preco_produtos"
#onde vai guardar uma listas de valores diferentes.
#Onde tem que criar um codigos que separes QUANTOS valores
#tem acima de R$20,00
#e por fim faça a soma de todos os valores da lista.

preco_produtos = [29.80, 8.50, 76.95, 16.79,45.50, 1.23]

contador_acima_de_20 = 0
total = 0

for preco in preco_produtos:
    total = total + preco
    if preco > 20.00:
        contador_acima_de_20 = contador_acima_de_20 + 1
print("Produtos acima de R$20,00: ", contador_acima_de_20)
print("Valor total da compra: ", total)