nome = str(input('Qual é o seu nome completo ? ')).strip()
print('Analisando seu nome...')
print('O seu nome em maiúscula é {}'.format(nome.upper()))
print('O seu nome em minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)- nome.count(' ')))
#print('Seu primeiro nome têm {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

