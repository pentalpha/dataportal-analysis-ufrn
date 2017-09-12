# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 19:14:05 2017

@author: Andre
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 17:34:21 2017

@author: Andre
"""

import csv
import matplotlib.pyplot as plt

dicAnos = {}
with open('bolsistas-de-iniciacao-cientifica.csv', encoding="utf8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    for row in readCSV:
        if(row[4] == "ano"):
            continue
        if(row[4] in dicAnos):    
            dicAnos[row[4]] += 1
        else:
            dicAnos[row[4]] = 0
            
maximo = max(dicAnos, key=dicAnos.get)
minimo = min(dicAnos, key=dicAnos.get)

print("O ano com menor quantidade de bolsas foi: " + minimo + " com " + str(dicAnos[minimo]) + " bolsas")
print("O ano com maior quantidade de bolsas foi: " + maximo + " com " + str(dicAnos[maximo]) + " bolsas")
print("A amplitude é: " + str(dicAnos[maximo]-dicAnos[minimo]))
