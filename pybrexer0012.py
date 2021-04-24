'''
     Solução para exercicios https://wiki.python.org.br/EstruturaSequencial
     #12) Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
          calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
'''

alturax = float(input('Digite a altura: '))
pesoideal = int((72.7 * alturax)-58)
print('O peso ideal para uma altura de {} é {} Kg.'.format(alturax, pesoideal))


