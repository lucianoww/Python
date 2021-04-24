'''
     #13) Tendo como dado de entrada a altura (h) de uma pessoa,
          construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
             a) Para homens: (72.7*h) - 58
             b) Para mulheres: (62.1*h) - 44.7
'''

erro = 0
texto = ''
pesoideal = 0.00
altura = 0.00

sexo = input('Informe sexo M (masculino) ou F (feminino): ').strip().upper()

#consistências

if not sexo.__eq__('M') and not sexo.__eq__('F'):
    erro = 1
    print('Só pode informar as letras M ou F')

if erro == 0:
    altura = float(input('Digite a altura: '))

if erro == 0 and altura == 0.00:
    erro = 1
    print('Altura deve ser maior que 0')

#fim consistencias


if erro == 0:
    if sexo.__eq__('F'):
        texto = 'Feminino'
        pesoideal = int((62.1*altura) - 44.7)

    if sexo.__eq__('M'):
        texto = 'Masculino'
        pesoideal = int((72.7 * altura) - 58)

    print('O peso ideal de uma pessoa do sexo {}, cuja altura é de {} é {} Kg.'.format(texto, altura, pesoideal))
