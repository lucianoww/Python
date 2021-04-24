'''
    #15) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
         Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11%
         para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
            a) salário bruto.
            b) quanto pagou ao INSS.
            c) quanto pagou ao sindicato.
            d) o salário líquido.
            e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
                + Salário Bruto : R$
                - IR (11%) : R$
                - INSS (8%) : R$
                - Sindicato ( 5%) : R$
                = Salário Liquido : R$
        Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
valorhora=0.00
numerohoras=0.00
salariobruto=0.00
perirf=11.00
perinss=8.00
persind=5.00
totalir=0.00
totalinss=0.00
totalsind=0.00
salarioliquido=0.00

valorhora=float(input('Valor por hora: '))
numerohoras=float(input('Total Horas Trabalhadas: '))
salariobruto=float(valorhora * numerohoras)

#deduções/descontos
totalir=salariobruto * (perirf/100)
totalinss=salariobruto * (perinss/100)
totalsind=salariobruto * (persind/100)

#salario liquido
salarioliquido= salariobruto - (totalir+totalinss+totalsind)

print(' (+) Salario bruto R$    {:10.2f}'.format(salariobruto))
print(' (-)            IR R$    {:10.2f}'.format(totalir))
print(' (-)          INSS R$    {:10.2f}'.format(totalinss))
print(' (-)     Sindicato R$    {:10.2f}'.format(totalsind))
print('                      -------------')
print('   Salário Liquido R$    {:10.2f}'.format(salarioliquido))




