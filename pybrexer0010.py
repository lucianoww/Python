'''
   Solução para exercicios https://wiki.python.org.br/EstruturaSequencial
   #10) Faça um Programa que peça a temperatura em graus Celcius,
       transforme e mostre a temperatura em graus ºF.
       C = 5 * ((F-32) / 9).
'''

tempc = float(input('Informe temperatura em ºC (Celsius) : '))
tempf = float((tempc * 1.800000) + 32)
print('{} ºC equivale a {} ºF'.format(tempc, tempf))