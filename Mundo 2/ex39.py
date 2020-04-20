'''ano = int(input('Ano de nascimento: '))
idad = 2020 - ano
soma = ano + 18
print('Quem nasceu em {} tem {} anos em 2020'.format(ano, idad))
if idad == 18:
    print('Você têm que se alistar nesse ano')
elif idad < 18:
    print('Você deverá se alistar apenas em {}'.format(soma))
    print('Ainda faltam {} anos'.format(soma - 2020))
else:
    print('Seu alistamento foi em {}'.format(soma))
    print('Há {} anos atrás'.format(2020 - soma))''' 'meu exemplo'

from datetime import date
atual = date.today().year
sexo = int(input('Digite o número [1] se for do gênero Masculino e [2] se for do gênero Feminino: '))
if sexo == 1:
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        print('Seu alistamento será em {}'.format(atual + saldo))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        print('Seu alistamento foi em {}.'.format(atual - saldo))
else:
    print('O alistamento OBRIGATÓRIO Brasileiro é somente para pessoas do sexo masculino')




