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

    for ano in anos:
        if(ano != "ano"):
            index = int(ano) - 2001
            if(index >= 0 and index <= 15):
                quantidade[index] += 1

    for ano in imd:
        if(ano != "ano"):
            index = int(ano)-2012
            if(index >= 0 and index <= 4):
                quantidadeIMD[index] += 1
            
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
