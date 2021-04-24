'''
     Solução para exercicios https://wiki.python.org.br/EstruturaSequencial
     #18) Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade
     de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo
     usando este link (em minutos).
'''

#unidades de tempo em segundos
dia = 86400
hor = 3600
min = 60

#uniades de armazenamento
tamByte = 8
cnvKB = 1024
cnvGB = 1000
cnvTB = 102400

tamArqMB = float(input('Informe tamanho do arquivo em Mb (Megabytes): '))
velDOWN = float(input('Informe velocidade em Mb/s: '))
tamArqGB = float(tamArqMB/cnvGB)
tamArqTB = float(tamArqMB/cnvTB)
velKBPS = float((velDOWN*cnvKB)/tamByte)
tamArqKB = (tamArqMB*cnvKB)
tempo = float(tamArqKB/velKBPS)

#Conversao de tempo em segundos para dia, hora, minuto, segundo
numdia = tempo // dia
segrst = tempo % dia
numhor = segrst // hor
segrst = segrst % hor
nummin = segrst // min
segrst = segrst % min

print(' > Velocidade Download. : {:.2f} Mbps'.format(velDOWN))
print(' > Velocidade em Kbps . : {:.0f} Kbps'.format(velKBPS))
print(' > Conversão de Mb p/Kb : {:.0f}'.format(tamArqKB))
print(' > Conversão de Mb p/Gb : {:.3f}'.format(tamArqGB))
print(' > Conversão de Mb p/Tb : {:.5f}'.format(tamArqTB))
print(' > Estimativa de tempo  : {:.0f} segundo(s) ou \n\t{:.0f} dia(s) {:.0f} hora(s) {:.0f} minuto(s) {:.0f} segundo(s)'
      .format(tempo, numdia, numhor, nummin, segrst))


