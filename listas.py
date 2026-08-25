numeros = [10, 20, 30, 40, 50]
print(numeros)

print(numeros[2])
print(numeros[0])
print(numeros[4])

print(len(numeros))
#len() mostra quantos elementos tem na lista

numeros.append(60) #adiciona um elemento no final
print(numeros)

numeros[2] = 70 #alterar o valor de um indice
print(numeros)

numeros.remove(50) #remove um elemento
print(numeros)