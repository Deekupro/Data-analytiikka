import pandas as pd

df1st = pd.read_csv('data/accidents_2005_to_2007.csv')
df2nd = pd.read_csv('data/accidents_2009_to_2011.csv')
df3rd = pd.read_csv('data/accidents_2012_to_2014.csv')


df = pd.concat([df1st, df2nd, df3rd], axis=0)

df.drop(columns=['Accident_Index','Location_Easting_OSGR', 'Location_Northing_OSGR', 'Longitude', 'Latitude', 'Police_Force', 'Local_Authority_(District)', 'Local_Authority_(Highway)', 'Did_Police_Officer_Attend_Scene_of_Accident'], inplace=True )