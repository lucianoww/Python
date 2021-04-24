'''
    #14) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
    trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
    São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
    João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
    Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa
    que João deverá pagar.
    Imprima os dados do programa com as mensagens adequadas.
'''

limite=50
multa=4.00
excesso=0.00
peso=0.00

peso=float(input('Informe o total em Kg: '))
excesso=peso-limite

if peso==0:
    print('Nossa!!! Que dia ruim de pesca. Volte outro dia pois ainta tem direito a {} Kg'
          .format(limite))
elif peso<=limite:
   print('Pesca abaixo do limite {} Kg. Quando quiser volte, pois tem direito a levar mais {} Kg.'
         .format(peso, limite-peso))
else:
    print('Pescaria com excesso de {} kg - aplicar multa R$ {}'
          .format(peso-limite, (peso-limite)*multa))



