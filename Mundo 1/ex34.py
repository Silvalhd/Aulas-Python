salário = float(input('Qual o salário do funcionário ? R$'))
n1 = (salário * 10/100) + salário
n2 = (salário * 15/100) + salário
if salário > 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R$ {:.2f}'.format(salário, n1))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salário, n2))
# Outro jeito de fazer:
"""if salário <= 1250:
    novo = salário + (salário * 15 / 100 )
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salário, novo))"""



