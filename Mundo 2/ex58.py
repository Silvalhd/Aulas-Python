#Meu exemplo
from random import randint
cont = 1
computador = randint(0, 10)
print('''Sou seu computador...
Acabei de pensei em um número entre 0 e 10.
Será que você consegue adivinhar qual foi ?''')
palp = int(input('Qual é seu palpite ? '))
while palp != computador:
    cont = cont + 1
    if palp < computador:
        print('Mais... Tente mais uma vez.')
        palp = int(input('Digite outro valor: '))
    else:
        print('Menos... Tente novamente...')
        palp = int(input('Digite outro valor: '))
print('Você acertou em {} tentativas, PARABÉNS !!!'.format(cont))

