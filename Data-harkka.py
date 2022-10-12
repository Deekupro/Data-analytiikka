import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats



# Luetaan data
df1 = pd.read_csv('data/accidents_2005_to_2007.csv')
df2 = pd.read_csv('data/accidents_2009_to_2011.csv')
df3 = pd.read_csv('data/accidents_2012_to_2014.csv')

# Yhdistetään data yhdeksi dataframeksi
df = pd.concat([df1, df2, df3], axis=0)


#lisää testausta dev_atte branch lisätty