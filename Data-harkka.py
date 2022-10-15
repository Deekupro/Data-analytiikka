import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from datetime import datetime


df = pd.read_csv('data/5000randomia.csv')
#df = pd.read_csv('data/cleaned_pt2_accidents_2005_to_2014.csv')
#muutetaan Date_time datetimeksi.
df['Date_time'] = pd.to_datetime(df['Date_time'])


#Tulostetaan onnettomuuksien määrä alkavalta tunnilta, esim 3:27 lasketaan 3.
hm=df.Date_time.dt.hour.value_counts().sort_index()
acc_per_hour = hm.plot(kind='bar')
acc_per_hour.set_ylabel('Onnettomuuksien määrä')
acc_per_hour.set_xlabel('Kellonaika')
plt.show()
#Huomataan, että eniten onnettomuuksia kello 8 ja 15-17, eli ruuhka ajat.


#Tehdään uusi sarake, jossa nimetään onnettomuuksien vakavuudet
Severity_Level = ['Fatal','Serious' ,'Minor']
df['Severity_Level'] = df['Accident_Severity'] 
df['Severity_Level'] = df['Severity_Level'].map(
                    {1:'Fatal',2:'Serious' ,3:'Minor'}) 

#selvitetään loukkaantumisten määrät
fatals=len(df[df['Severity_Level']=='Fatal'])
serious=len(df[df['Severity_Level']=='Serious'])
minors=len(df[df['Severity_Level']=='Minor'])

#Tehdään piirakka-kaavio jossa näkyy vammojen asteet ja prosenttiosuudet
acc_by_sev = df['Severity_Level'].value_counts()
acc_by_sev.plot(kind='pie', ylabel='', labels=['Minor', 'Serious','Fatal'],
         title=f'Minor injuries: {minors}\n Serious injuries:  {serious}\n Fatalities: {fatals}',
         startangle=270, autopct='%1.1f%%')
plt.show()
#Huomataan, että paljon lieviä vammoja verrattuna muihin


#Tehdään histogrammi, jossa näkyvät vuosittaisten onnettomuuksien määrät
years = np.unique(df['Year'])
acc_by_year = df.Year.value_counts().sort_index()
barplot=plt.bar(x=years, height=acc_by_year)
plt.bar_label(barplot, labels=acc_by_year, label_type="edge")
plt.show()
#Onnettomuudet ovat vähenemään päin


#Tutkitaan minä viikonpäivänä tapahtuu eniten onnettomuuksia.
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
acc_by_day = df.Day_of_Week.value_counts().sort_index()
barplot=plt.bar(x=days, height=acc_by_day)
plt.bar_label(barplot, labels=acc_by_day, label_type="edge")
plt.show()
#Eniten onnettomuuksia tapahtuu lauantaisin.

#Selvitetään milla nopeus alueella tapahtuu eniten onnettomuuksia
limit = np.unique(df['Speed_limit'])
acc_by_limit = df.Speed_limit.value_counts().sort_index()
barplot=plt.bar(x=limit, height=acc_by_limit)
plt.bar_label(barplot, labels=acc_by_limit, label_type="edge")
plt.show()