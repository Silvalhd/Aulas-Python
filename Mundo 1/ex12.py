p = float(input('Qual o preço do produto ? R$'))
p2 = float(input('Qual a porcentagem do desconto ? %'))
n = p-(p*p2/100)
print('O produto que custava R${:.2f}, na promoção com desconto de {:.0f}% vai custar R${:.2f}.'.format(p, p2, n))