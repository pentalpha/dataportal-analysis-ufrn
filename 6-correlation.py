#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 01:10:31 2017

@author: pitagoras
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

np.random.seed(int(datetime.now().day + datetime.now().second))

sns.set(color_codes=True)

df = pd.read_csv("pesquisadores.csv", sep=";")
df['totalProjetos'] = df.apply(lambda row: row['internos']+row['externos'],
  axis=1)
plot = sns.lmplot(x="internos", y="externos", data=df, 
                  x_jitter=0.2, y_jitter=0.21, robust=False);
plot2 = sns.lmplot(x="totalProjetos", y="coordenador", data=df, 
                  x_jitter=0.2, y_jitter=0.21, order=3);