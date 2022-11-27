from time import sleep

def contador(i,f,p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p} ')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.1)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.1)
            cont -= p
        print('FIM')
    print('-=' * 20)

##Programa Principal
contador(1,10,1)
contador(10,1,1)