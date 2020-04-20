#Meu exemplo
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while not op == 5:
    sleep(0.8)
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    op = int(input('>>>> Qual é a sua opção ? '))
    if op == 1:
        s = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, s))
        print('-=-' * 10)
    elif op == 2:
        m = n1 * n2
        print('O resultado de {} x {} é {:.1f}'.format(n1, n2, m))
        print('-=-' * 10)
    elif op == 3:
        if n1 > n2:
            print('O primeiro valor é maior que o segundo')
            print('-=-' * 10)
        else:
            print('O segundo valor é maior que o primeiro')
            print('-=-' * 10)
    elif op == 4:
        n1 = int(input('Digite o primeiro novo valor: '))
        n2 = int(input('Digite o segundo novo valor: '))
    elif op == 5:
        print('Fim do programa')
    else:
        print('Comando inválido, escolha novamente')
        print('-=-' * 10)
print('-=-' * 10)





