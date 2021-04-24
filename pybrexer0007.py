'''
    Solução para exercicios https://wiki.python.org.br/EstruturaSequencial
    #07) Faça um Programa que calcule a área de um quadrado,
         em seguida mostre o dobro desta área para o usuário.
'''

comprimentox=float(input('Digite o comprimento :'))
largurax=float(input('Digite a largura :'))
areax=comprimentox*largurax
print('Uma área com {} de comprimento por {} de largura possui uma area total de {} em m²'
      .format(comprimentox, largurax, areax))
print('O dobro desta área em m²: {}'.format(areax*2))