# Programa que calcula a média aritimética de cinco notas digitadas pelo usuário;

media = 0
for x in range(5):
    nota = float(input("Insira sua nota: "))
    media = media + nota

media = media / 5
print(media)









# Programa que calcula a média aritimética de cinco notas digitadas pelo usuário; masi complexo

a = int(input("Insira o valor da primeira nota: "))
b = int(input("Insira o valor da segunda nota: "))
c = int(input("Insira o valor da terceira nota: "))
d = int(input("Insira o valor da quarta nota: "))
e = int(input("Insira o valor da quinta nota: "))

media = (a + b + c + d + e) / 5
print(media)