'''
    Solução para exercicios https://wiki.python.org.br/EstruturaSequencial
    #04)Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''
nota1 = float(input('Informar nota 1:'))
nota2 = float(input('Informar nota 2:'))
nota3 = float(input('Informar nota 3:'))
nota4 = float(input('Informar nota 4:'))
soma=nota1+nota2+nota3+nota4
print('{} + {} + {} + {} = {} - Media {}'.format(nota1, nota2, nota3, nota4, soma, (soma/4)))