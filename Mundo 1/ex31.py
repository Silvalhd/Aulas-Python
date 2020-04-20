num = float(input('Qual a distância da viagem em Km ?'))
n1 = num*0.50
n2 = num*0.45
if num <= 200:
    print('Prezado viajante sua passagem custará R${:.2f}'.format(n1))
else:
    print('Prezado viajante sua passagem custará R${:.2f}'.format(n2))
