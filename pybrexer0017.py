'''
     #17) Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
          da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
          e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros,
          que custam R$ 25,00.
          Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
                 comprar apenas latas de 18 litros;
                 comprar apenas galões de 3,6 litros;
                 misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga
                 e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

area= float(input('Digite area em m²: '))
margem=float(10/100)
metros=6.00
numerogalao=0.00
excedente=0.00
custototal1=0.00
custototal2=0.00
custototal3=0.00

#dados galão 18L
lata1=18.00
custo1=80.00

#dados galao 3.6L
lata2=3.60
custo2=25.00

totallitros1=float(area/metros)+((100+margem)/100)
numerolatas1=(totallitros1/lata1).__ceil__()
custototal1=(numerolatas1*custo1)

totallitros2=float(area/metros)+((100+margem)/100)
numerolatas2=(totallitros2/lata2).__ceil__()
custototal2=(numerolatas2*custo2)


print('<<<Opção 1: Galões de 18L >>> ')
print('     Total de litros . : {:10.2f} '.format(totallitros1))
print('     Latas necessarias : {:10.2f} '.format(numerolatas1))
print('     Preço unitário. . : {:10.2f} '.format(custo1))
print('\n   Preço total . . . : {:10.2f} '.format(custototal1))

print('\n<<<Opção 2: Galões de 3.6L >>> ')
print('     Total de litros . : {:10.2f} '.format(totallitros2))
print('     Latas necessarias : {:10.2f} '.format(numerolatas2))
print('     Preço unitário. . : {:10.2f} '.format(custo2))
print('     Preço total . . . : {:10.2f} '.format(custototal2))

if totallitros1 > 18.00:
    excedente = (totallitros1 - 18.00)
    totallitros1 = 18.00
    numerolatas1 = int(totallitros1 / lata1)
    custototal1 = (numerolatas1 * custo1)

    totallitros2 = excedente
    numerolatas2 = (totallitros2 / lata2).__ceil__()
    custototal2 = (numerolatas2 * custo2)

    print('\n<<< Opção 3: Galões de 18L e 3.6L >>> ')

    print('     Total de litros . . : {:10.2f} '.format(totallitros1))
    print('     Latas 18L. .. . . . : {:10.2f} '.format(numerolatas1))
    print('     Preço unitário. . . : {:10.2f} '.format(custo1))
    print('     Cobrira uma area de : {:10.2f} m²'.format(totallitros1 * metros))
    print('     Subtotal. . . . . . : {:10.2f} '.format(custototal1))

    print('\n     Total de litros . . : {:10.2f} '.format(excedente))
    print('     Latas 3.6L. .  . .  : {:10.2f} '.format(numerolatas2))
    print('     Preço unitário. . . : {:10.2f} '.format(custo2))
    print('     Cobrira uma area de : {:10.2f} m²'.format(excedente * metros))
    print('     Subtotal. . . . . . : {:10.2f} '.format(custototal2))
    print('\n    Total. . . . . . . . : {:10.2f} '.format( custototal1 + custototal2))

if (custototal1 < custototal2 and custototal1 < custototal3):
    print('\n <<< Menor custo/beneficio é Opção 1 >>>')
elif (custototal2 < custototal1 and custototal2 < custototal3):
    print('\n <<< Menor custo/beneficio é Opção 2 >>>')
else:
    print('\n <<< Menor custo/beneficio é Opção 3 >>>')











