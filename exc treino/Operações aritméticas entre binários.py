try:
    nu1 = str(input("Insira o valor do primeiro número: "))
    nu2 = str(input("Insira o valor do segundo número: "))

    soma = bin(int(nu1, 2) + int(nu2, 2))
    sub = bin(int(nu1, 2) - int(nu2, 2))
    mult = bin(int(nu1, 2) * int(nu2, 2))
    div = bin(int(nu1, 2) // int(nu2, 2))

    print("""[ 1 ] Adicão
    [ 2 ] Subtração
    [ 3 ] Multiplicação
    [ 4 ] Divisão""")
    opção = int(input("Escolha sua operação de 1 a 4: "))

    if opção == 1:
        print(soma[2:])
    elif opção == 2:
        print(sub[2:])
    elif opção == 3:
        print(mult[2:])
    elif (nu1 != 0 and nu2 !=0) and (opção == 4):
        print(div[2:])
    else:
        print("Digite um número de 1 a 4: ")

except ZeroDivisionError:
    print("ERROR TENTE NOVAMENTE")
