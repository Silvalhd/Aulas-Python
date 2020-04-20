print('{:= ^ 40}'.format(' LOJAS GUANABARA '))
p = float(input('Preços das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual é a opção ? '))
if op == 1:
    total = p - (p * 10 / 100)
elif op == 2:
    total = p - (p * 5 / 100)
elif op == 3:
    total = p
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}, SEM JUROS'.format(parcela))
elif op == 4:
    total = p + (p * 20 / 100)
    totparc = int(input('Quantas parcelas ? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${}, COM JUROS'.format(totparc, parcela))
else:
    total = p
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, total))



