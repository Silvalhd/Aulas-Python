n = float(input('Qual é a velocidade atual do carro ?'))
multa = (n-80)*7.00
if n > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${}'.format(multa))
print('Tenha um bom dia! Dirija com segurança')
