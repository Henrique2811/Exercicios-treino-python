# Programa que le um valor e imprime a quantidade de cédulas para pagar o valor. 
# Para simplificar, vamos trabalhar apenas com valores inteiros 
# e com cédulas de R$50, R$20, R$10, R$5 e R$1;

x = int(input("Insira um valor: "))
cedulas = 0
nota = 50

while nota > 0:
    if x >= nota:
        x = x - nota
        cedulas = cedulas + 1
    else:
        if cedulas != 0:
            print(f"Precisa de {cedulas} cédulas de {nota}")
            cedulas = 0
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5 
        elif nota == 5:
            nota = 1
        elif nota == 1:
            nota = 0
