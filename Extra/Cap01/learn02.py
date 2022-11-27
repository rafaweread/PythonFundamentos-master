nome = input("Digite seu nome: ")
tamanho = len(nome)
print(tamanho)
print(type(tamanho))

if tamanho % 2 == 0:
    print("Tamanho do seu nome representa valor par!")
elif tamanho % 2 != 0:
    print("Tamanho do seu nome representa valor impar!")


