'''
    Solução para exercicios https://wiki.python.org.br/EstruturaSequencial
    #06) Faça um Programa que peça o raio de um círculo, calcule e mostre sua área
'''

vlrpi=3.141592
raiox = int(input('Digite o raio do circulo:'))
print('Um circulo com raio de {} possui uma area de {}'.format(raiox, float(vlrpi*(raiox.__pow__(2)))))