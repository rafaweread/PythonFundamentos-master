def calculaValor(valor):
    if valor >= 10 or valor >= 30:
        for i in range(1):
            print("O valor ",valor,"digitado esta entre 10 e 30 ")

x = int(input("Digite um valor: "))
calculaValor(x)