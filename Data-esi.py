import pandas as pd
import numpy as np
from datetime import datetime


#Luetaan data omiin dataframeihin
df1 = pd.read_csv('accidents_2005_to_2007.csv')
df2 = pd.read_csv('accidents_2009_to_2011.csv')
df3 = pd.read_csv('accidents_2012_to_2014.csv')

#Ydistetään dataframet Frameen
frames = [df1, df2, df3]

#Tehdään yksi iso dataframe
df = pd.concat(frames)

#Tiputetaan pois tietyt sarakkeet
df.drop(columns= ['Junction_Detail','Location_Easting_OSGR','Location_Northing_OSGR'], inplace=True)
df.drop(columns= ['Longitude','Latitude','Police_Force','LocalAuthority(District)'], inplace=True)
df.drop(columns= ['LocalAuthority(Highway)','Did_Police_Officer_Attend_Scene_of_Accident','LSOA_of_Accident_Location'], inplace=True)

#yhdistetään Date ja Time, sekä muutetaan datetime muotoon
df['Date_time'] = pd.to_datetime(df.Date + ' ' +df.Time)


#Tässä sarakkeessa 600 000 nan arvoa, joten muutamme arvot None arvoksi
df['Junction_Control'] = df['Junction_Control'].replace(np.NAN, 'None')

#Täytyy tehä uusi dataframe, jotta 
df4 = df.dropna()


#Tarkistetaan onko nan arvoja
print(df.isna().sum())
#Ei nan arvoja.

#Datasetti on siivottu


df4.to_csv('testi.csv')
