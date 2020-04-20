peso = float(input('Qual é o seu peso ? (Kg) '))
altura = float(input('Qual é a sua altura ? (m) '))
imc = peso/(altura**2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você esta com SOBREPESO!')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('Cuidado, você está com OBSiDADE MÓBIDA!')


