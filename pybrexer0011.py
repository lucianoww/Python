'''
    Solução para exercicios https://wiki.python.org.br/EstruturaSequencial
    #11) Faça um Programa que peça 2 números inteiros e um número real.
         Calcule e mostre:
         a) o produto do dobro do primeiro com metade do segundo .
         b) a soma do triplo do primeiro com o terceiro.
         c) o terceiro elevado ao cubo.
'''
valor1 = int(input('Informe valor 1: '))
valor2 = int(input('Informe Valor 2: '))
valor3 = float(input('Informe Valor 3: '))
print('Dobro do primeiro: {}', valor1*2)
print('Metade do segundo: {}', valor2/2)
print('a) Produto entre primeiro e segundo: {}'.format(((valor1*2) * (valor2/2))))
print('b) Soma triplo do primeiro + terceiro: {} '.format( (valor1*3) + valor3 ))
print('c) Terceiro elevado ao cubo: {}'.format( valor3.__pow__(3)))



