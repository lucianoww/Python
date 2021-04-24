'''
     #16) Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
          em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
          é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
          18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de
          tinta a serem compradas e o preço total.
'''

area= float(input('Digite area em m²: '))
metrosl=3.00
totallitros=float(area/metrosl)
lata=18.00
numerolatas=totallitros/lata
custol=80.00

print('Total de litros . : {:10.2f} '.format(totallitros))
print('Latas necessarias : {:10.2f} '.format(numerolatas))
print('Preço total . . . : {:10.2f} '.format((numerolatas*custol)))


