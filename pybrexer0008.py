'''
     Solução para exercicios https://wiki.python.org.br/EstruturaSequencial
     #08) Faça um Programa que pergunte quanto você ganha por hora e o
          número de horas trabalhadas no mês. Calcule e mostre o total
          do seu salário no referido mês.
'''

valorh = float(input('Informe valor/hora:'))
numeroh = float(input('Informe número horas trabalhadas no mês:'))
salario = valorh*numeroh
print('Você ganha {} por hora, se neste mês trabalhou {} então receberá R$ {}'.format(valorh, numeroh, salario))