print("""################################
            Calculadora
################################
    Escolha uma opção:

    1) Multiplicação
    2) Soma
    3) Divisão"""

)

opcao = input(int())

if opcao == 1:
    def calculadora(x,y):
        return (x * y)

    resultado = calculadora(2,4)
    print(resultado)
