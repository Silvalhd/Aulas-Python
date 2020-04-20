frase = str(input('Digite uma Frase: ')).upper().strip().replace('Â', 'A').replace('Ã', 'A').replace('À', 'A')
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))