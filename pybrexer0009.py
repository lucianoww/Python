'''
    Solução para exercicios https://wiki.python.org.br/EstruturaSequencial
    #09) Faça um Programa que peça a temperatura em graus Fahrenheit,
         transforme e mostre a temperatura em graus Celsius.
         C = 5 * ((F-32) / 9).
'''

tempf = float(input('Informe temperatura em ºF (Fahrenheit) : '))
tempc = float(5 * ((tempf-32) / 9))
print('{} ºF equivale a {} ºC'.format(tempf, tempc))