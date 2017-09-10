import csv
import numpy as np
from matplotlib import pyplot as plt

anos = []
imd = []
quantidade = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
quantidadeIMD = [0, 0, 0, 0, 0]
with open('bolsistas-de-iniciacao-cientifica.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\t')
    for row in readCSV:
         anos.append(row[4])
         if row[13] == 'INSTITUTO METROPOLE DIGITAL - IMD':
            imd.append(row[4])
    
    for i in range(0, len(anos)):
        if anos[i] == '2001':
            quantidade[0] = (quantidade[0]+1)
        if anos[i] == '2002':
            quantidade[1] = (quantidade[1]+1)
        if anos[i] == '2003':
            quantidade[2] = (quantidade[2]+1)
        if anos[i] == '2004':
            quantidade[3] = (quantidade[3]+1)
        if anos[i] == '2005':
            quantidade[4] = (quantidade[4]+1)
        if anos[i] == '2006':
            quantidade[5] = (quantidade[5]+1)
        if anos[i] == '2007':
            quantidade[6] = (quantidade[6]+1)
        if anos[i] == '2008':
            quantidade[7] = (quantidade[7]+1)
        if anos[i] == '2009':
            quantidade[8] = (quantidade[8]+1)
        if anos[i] == '2010':
            quantidade[9] = (quantidade[9]+1)
        if anos[i] == '2011':
            quantidade[10] = (quantidade[10]+1)
        if anos[i] == '2012':
            quantidade[11] = (quantidade[11]+1)
        if anos[i] == '2013':
            quantidade[12] = (quantidade[12]+1)
        if anos[i] == '2014':
            quantidade[13] = (quantidade[13]+1)
        if anos[i] == '2015':
            quantidade[14] = (quantidade[14]+1)
        if anos[i] == '2016':
            quantidade[15] = (quantidade[15]+1)
            
    for i in range(0, len(imd)):
        if imd[i] == '2012':
            quantidadeIMD[0] = (quantidadeIMD[0]+1)
        if imd[i] == '2013':
            quantidadeIMD[1] = (quantidadeIMD[1]+1)
        if imd[i] == '2014':
            quantidadeIMD[2] = (quantidadeIMD[2]+1)
        if imd[i] == '2015':
            quantidadeIMD[3] = (quantidadeIMD[3]+1)
        if imd[i] == '2016':
            quantidadeIMD[4] = (quantidadeIMD[4]+1)
            
#Tirei 2017 por que o ano ainda n acabou e a bse de dados n tem os artigos de 2017, então n ajudaria na analise do gráfico         
xs = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,
      2012,2013,2014,2015,2016]
#print len(anos)
#print len(imd)
plt.title("Grafico de Linha de artigos publicados da UFRN") 
plt.ylabel("Quantidade de artigos")
plt.xlabel("anos")
plt.plot(xs,quantidade,'g-')
plt.show()

xz = [2012,2013,2014,2015,2016]
plt.title("Grafico de Linha de artigos publicados do IMD") 
plt.ylabel("Quantidade de artigos")
plt.xlabel("anos")
plt.plot(np.arange(len(xz)),quantidadeIMD,'g-')
plt.xticks(np.arange(len(xz)), xz)


plt.show()
    