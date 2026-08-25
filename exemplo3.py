#Faça um programa que só valide entrada do usuário, 
# se ele digitar um numero positivo.
numero = int(input("Digite um numero: "))

while numero <= 0:
    print("numero invalido, tente novamente!")
    numero = int(input("Digite o numero novamente: "))
print("Obrigado, você digitou o numero positivo: ", numero)