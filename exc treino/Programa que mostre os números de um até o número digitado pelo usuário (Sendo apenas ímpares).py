# Escreva um programa que mostre os números de um até o número digitado pelo usuário, 
# mas, apenas os númers ímpares;

numero = int(input("Insira o número ímpar: "))
for x in range(1, numero, 2):
    print(x)
