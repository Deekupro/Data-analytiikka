import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats


df = pd.read_csv('data/5000randomia.csv')
#df = pd.read_csv('data/cleaned_pt2_accidents_2005_to_2014.csv')
#muutetaan Date_time datetimeksi.
df['Date_time'] = pd.to_datetime(df['Date_time'])

df.info()
print(df.Weather_Conditions.unique())
#df['Weather_Conditions'].astype(str).astype(int)



# =============================================================================
# #Tulostetaan onnettomuuksien määrä alkavalta tunnilta, esim 3:27 lasketaan 3.
# hm=df.Date_time.dt.hour.value_counts().sort_index()
# acc_per_hour = hm.plot(kind='bar')
# acc_per_hour.set_ylabel('Onnettomuuksien määrä')
# acc_per_hour.set_xlabel('Kellonaika')
# plt.show()
# #Huomataan, että eniten onnettomuuksia kello 8 ja 15-17, eli ruuhka ajat.
# 
# 
# #Tehdään uusi sarake, jossa nimetään onnettomuuksien vakavuudet
# Severity_Level = ['Fatal','Serious' ,'Minor']
# df['Severity_Level'] = df['Accident_Severity'] 
# df['Severity_Level'] = df['Severity_Level'].map(
#                     {1:'Fatal',2:'Serious' ,3:'Minor'}) 
# 
# #selvitetään loukkaantumisten määrät
# fatals=len(df[df['Severity_Level']=='Fatal'])
# serious=len(df[df['Severity_Level']=='Serious'])
# minors=len(df[df['Severity_Level']=='Minor'])
# 
# #Tehdään piirakka-kaavio jossa näkyy vammojen asteet ja prosenttiosuudet
# acc_by_sev = df['Severity_Level'].value_counts()
# acc_by_sev.plot(kind='pie', ylabel='', labels=['Minor', 'Serious','Fatal'],
#          title=f'Minor injuries: {minors}\n Serious injuries:  {serious}\n Fatalities: {fatals}',
#          startangle=270, autopct='%1.1f%%')
# plt.show()
# #Huomataan, että paljon lieviä vammoja verrattuna muihin
# 
# 
# #Tehdään histogrammi, jossa näkyvät vuosittaisten onnettomuuksien määrät
# years = np.unique(df['Year'])
# acc_by_year = df.Year.value_counts().sort_index()
# barplot=plt.bar(x=years, height=acc_by_year)
# plt.bar_label(barplot, labels=acc_by_year, label_type="edge")
# plt.show()
# #Onnettomuudet ovat vähenemään päin
# 
# 
# #Tutkitaan minä viikonpäivänä tapahtuu eniten onnettomuuksia.
# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# acc_by_day = df.Day_of_Week.value_counts().sort_index()
# barplot=plt.bar(x=days, height=acc_by_day)
# plt.bar_label(barplot, labels=acc_by_day, label_type="edge")
# plt.show()
# #Eniten onnettomuuksia tapahtuu lauantaisin.
# 
# 
# #Selvitetään milla nopeus alueella tapahtuu eniten onnettomuuksia
# limit = np.unique(df['Speed_limit'])
# acc_by_limit = df.Speed_limit.value_counts().sort_index()
# barplot=plt.bar(x=limit, height=acc_by_limit)
# plt.bar_label(barplot, labels=acc_by_limit, label_type="edge")
# plt.show()
# 
# 
# #Korrelaatio
#Uusi df korrelaatiota varten
df_corr = df.loc[:, ['Accident_Severity', 'Date_time', 'Day_of_Week', 'Road_Type', 'Speed_limit',
                      'Light_Conditions', 'Weather_Conditions', 'Road_Surface_Conditions']]

Weather_num = ['Raining with high winds' 'Fine without high winds' 'Other']
 #'Raining without high winds' 'Fine with high winds'
 #'Snowing with high winds' 'Fog or mist' 'Unknown'
 #'Snowing without high winds']
df['Weather_num'] = df['Weather_Conditions'] 
df['Weather_num'] = df['Weather_num'].map(
                    {1: 'Raining with high winds', 2: 'Fine without high winds',
                     3: 'Other'})

corr = df_corr.corr()
print(df_corr.corr())
sns.heatmap(corr, annot=True, vmin=-0.2, vmax=1)
plt.show()

#Korrelaatio vakavuuden ja sääolosuhteiden välillä (Pearson)
r,p = stats.pearsonr(df_corr['Accident_Severity'], df_corr['Weather_Conditions'])
print(r)
print(p)

#Korrelaatio vakavuuden ja sääolosuhteiden välillä (Spearman)
r,p = stats.spearmanr(df_corr['Accident_Severity'], df_corr['Weather_Conditions'])
print (r)
print(p)

#Regressiosuora
reg_suora = sns.regplot(x=df_corr['Accident_Severity'], y=df_corr['Weather_Conditions'], data=df_corr)
plt.show()

<<<<<<< HEAD
=======

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

#Luodaan dataframet jossa vain tietyt loukkaantumiset.
fatal_accidents = df[df['Accident_Severity'] == 1]
serious_accidents = df[df['Accident_Severity'] == 2]
minor_accidents = df[df['Accident_Severity'] == 3]

#Tutkitaan kuolemaan johtaneita onnettomuuksia nopeusalueen mukaan
fatal_limit = np.unique(fatal_accidents['Speed_limit'])
fatal_acc_by_limit = fatal_accidents.Speed_limit.value_counts().sort_index()
barplot=plt.bar(x=fatal_limit, height=fatal_acc_by_limit)
plt.title('Kuolemaan johtaneet')
plt.bar_label(barplot, labels=fatal_acc_by_limit, label_type="edge")
plt.show()


#Tutkitaan vakavia onnettomuuksia nopeusalueen mukaan
serious_limit = np.unique(serious_accidents['Speed_limit'])
serious_acc_by_limit = serious_accidents.Speed_limit.value_counts().sort_index()
barplot=plt.bar(x=serious_limit, height=serious_acc_by_limit)
plt.title('Vakaviin vammoihin johtaneet')
plt.bar_label(barplot, labels=serious_acc_by_limit, label_type="edge")
plt.show()


#Tutkitaan lieviä onnettomuuksia nopeusalueen mukaan
minor_limit = np.unique(minor_accidents['Speed_limit'])
minor_acc_by_limit = minor_accidents.Speed_limit.value_counts().sort_index()
barplot=plt.bar(x=minor_limit, height=minor_acc_by_limit)
plt.title('Lieviin vammoihin johtaneet')
plt.bar_label(barplot, labels=minor_acc_by_limit, label_type="edge")
plt.show()

#Tutkitaan kuinka iso prosentti osuus kuolemaan johtaneista tapahtuu tietyllä tie tyylillä
print(fatal_accidents.Road_Type.value_counts()/fatal_accidents.shape[0])
print(serious_accidents.Road_Type.value_counts()/serious_accidents.shape[0])
print(minor_accidents.Road_Type.value_counts()/minor_accidents.shape[0])
>>>>>>> f2e93b15fe63082c7ecbcc156af85e4730814826
