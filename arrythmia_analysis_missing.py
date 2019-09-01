# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 04:54:25 2019

@author: yehadji
"""

#%%

#Missing data visualization in the Arrhythmia dataset


#%%
import time
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import matplotlib.pyplot as plp
import seaborn as sns
import matplotlib.gridspec as gridspec
import missingno as msno
from scipy import stats
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LassoLarsCV, LassoLarsIC
import os
#%%
# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
cwd
# Change directory
os.chdir(r"C:\Users\yehadji\Documents\MCS\MCS 02\Arrhythmia Data Set")
#%%
df_original = pd.read_csv(r"C:\Users\yehadji\Documents\MCS\MCS 02\Arrhythmia Data Set\arrhythmia.csv", 
                 na_values=['?'], delimiter = ";")

#%%
missingdata = df_original.columns[df_original.isnull().any()].tolist()
fig1 = msno.matrix(df_original[missingdata], figsize=(30,20)) #nullity matrix
fig1.plot()
plt.savefig('missing1.jpg')
#
fig2 = msno.bar(df_original[missingdata], color="blue", log=True, figsize=(30,20))#bar chart visualization of the data nullity
fig2.plot()
plt.savefig('missing2.jpg')
#%
fig3 = msno.heatmap(df_original[missingdata], figsize=(30,20)) #correlation heatmap
fig3.plot()
plt.savefig('missing3.jpg')


#%%
#%%