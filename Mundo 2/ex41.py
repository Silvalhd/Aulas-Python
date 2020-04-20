from datetime import date
atual = date.today().year
nasc = int(input('Qual é o ano do seu nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('O atleta esta na categoria MIRIM')
elif idade <= 14:
    print('O atleta está na categoria INFANTIL')
elif idade <= 19:
    print('O atleta está na categoria JUNIOR')
elif idade <= 25:
    print('O atleta está na cetegoria SÊNIOR')
else:
    print('O atleta está na categoria MASTER')

