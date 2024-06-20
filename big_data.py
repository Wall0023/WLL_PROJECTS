x = 0
palavra = str(input('Digite o texto: '))
try:
    qnt = int(input('Insira o número de unidades:'))
except ValueError:
    print('O valor precisa ser um inteiro')
while x < qnt:
    x+=1
    print('{}{},'.format(palavra,x))