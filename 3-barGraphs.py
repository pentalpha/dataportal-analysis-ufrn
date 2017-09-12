import csv
import numpy as np
from matplotlib import pyplot as plt

situacao = []
quantidade = [0, 0, 0]

with open('bolsistas-de-iniciacao-cientifica.csv',encoding="utf8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\t')
    for row in readCSV:
         situacao.append(row[14])
    #print len(situacao)
    
    for i in range(0, len(situacao)):
        if situacao[i] == 'FINALIZADO':
            quantidade[0] = (quantidade[0]+1)
        if situacao[i] == 'EM ANDAMENTO':
            quantidade[1] = (quantidade[1]+1)
        if situacao[i] == 'PENDENTE DE RELATORIO':
            quantidade[2] = (quantidade[2]+1)
    aux = ['Finalizado','Andamento', 'Pendente']        
    #print quantidade
    y_pos = np.arange(len(aux))
    plt.bar(y_pos, quantidade)
    plt.xticks(y_pos, aux)
    plt.title("Grafico de barras da situacao dos artigos")
    plt.ylabel('Quantidade de artigos')
    plt.show()
