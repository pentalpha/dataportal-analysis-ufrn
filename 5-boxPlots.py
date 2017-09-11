#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 01:10:31 2017

@author: pitagoras
"""

import numpy as np
import pandas as pd
from bokeh.charts import BoxPlot, output_notebook, show

df = pd.read_csv("projetos-de-pesquisa.csv", sep="\";\"")
df["ano"] = df["ano"].apply(pd.to_numeric, errors='coerce')

unidades = set()
unidadeInternalProjects = dict()
unidadeExternalProjects = dict()

def countProjectsByUnidade(row):
    if(row["tipo_projeto"] == "INTERNO"):
        unidadeInternalProjects[row["unidade"]] += 1
    elif(row["tipo_projeto"] == "EXTERNO"):
        unidadeExternalProjects[row["unidade"]] += 1

def projectsBoxplot(df, year=-2000, specificTypes=True):
    df = df[df.ano >= year]    
    for unidade in df.unidade.unique():
        unidades.add(unidade)
        unidadeInternalProjects[unidade] = 0
        unidadeExternalProjects[unidade] = 0
        
    df.apply(lambda row: countProjectsByUnidade(row), axis=1)
    
    rows = []
    for unidade in unidades:
        if(specificTypes):
            newRow = dict()
            newRow["unidade"] = unidade
            newRow["projType"] = "INTERNO"
            newRow["count"] = unidadeInternalProjects[unidade]
            rows.append(newRow)
            
            newRow = dict()
            newRow["unidade"] = unidade
            newRow["projType"] = "EXTERNO"
            newRow["count"] = unidadeExternalProjects[unidade]
            rows.append(newRow)
        else:
            newRow = dict()
            newRow["unidade"] = unidade
            newRow["projType"] = "TODOS"
            newRow["count"] = unidadeExternalProjects[unidade] + unidadeInternalProjects[unidade] 
            rows.append(newRow)
        
    unidadesDf = pd.DataFrame(rows, columns=["unidade", "projType",
                                             "count"])
    p = BoxPlot(unidadesDf, values='count', label="projType", color="projType",
                whisker_color='goldenrod', title="Projetos em Unidades da UFRN")
    #output_notebook()
    show(p)

projectsBoxplot(df, year=2015)
projectsBoxplot(df, year=2015, specificTypes=False)