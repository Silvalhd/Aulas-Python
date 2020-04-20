from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "pensar"
print('-=-' *20)
nome = input('Qual é o seu nome ? ')
print('Olá {}! vamos jogar ? \nVou pensar em um número entre 0 e 5 e tente adivinhar...'.format(nome))
print('-=-' * 20)
jogador = int(input('Em que número pensei ? '))# Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador :
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('VOCÊ PERDEU! Eu pensei no número {} e não no {}!'.format(computador, jogador))



