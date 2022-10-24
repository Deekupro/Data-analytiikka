import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.preprocessing import LabelEncoder

<<<<<<< HEAD

=======
>>>>>>> main
#df = pd.read_csv('data/5000randomia.csv')
df = pd.read_csv('data/cleaned_pt2_accidents_2005_to_2014.csv')
#muutetaan Date_time datetimeksi.
df['Date_time'] = pd.to_datetime(df['Date_time'])


#Tulostetaan onnettomuuksien määrä alkavalta tunnilta, esim 3:27 lasketaan 3.
hm=df.Date_time.dt.hour.value_counts().sort_index()
acc_per_hour = hm.plot(kind='bar')
acc_per_hour.set_ylabel('Onnettomuuksien määrä')
acc_per_hour.set_xlabel('Kellonaika')
plt.title('Onnettomuudet kellonajan mukaan')
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
plt.title('Loukkaantumiset vakavuuden mukaan prosentuaalisesti')
plt.show()
#Huomataan, että paljon lieviä vammoja verrattuna muihin


#Tehdään histogrammi, jossa näkyvät vuosittaisten onnettomuuksien määrät
years = np.unique(df['Year'])
acc_by_year = df.Year.value_counts().sort_index()
barplot=plt.bar(x=years, height=acc_by_year)
plt.bar_label(barplot, labels=acc_by_year, label_type="edge")
plt.title('Onnettomuudet vuosittain')
plt.show()
#Onnettomuudet ovat vähenemään päin


#Tutkitaan minä viikonpäivänä tapahtuu eniten onnettomuuksia.
<<<<<<< HEAD
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
=======
days = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
>>>>>>> main
acc_by_day = df.Day_of_Week.value_counts().sort_index()
barplot=plt.bar(x=days, height=acc_by_day)
plt.bar_label(barplot, labels=acc_by_day, label_type="edge")
plt.title('Onnettomuudet viikonpäivän mukaan')
plt.show()
#Eniten onnettomuuksia tapahtuu lauantaisin.


#Selvitetään milla nopeus alueella tapahtuu eniten onnettomuuksia
limit = np.unique(df['Speed_limit'])
acc_by_limit = df.Speed_limit.value_counts().sort_index()
barplot=plt.bar(x=limit, height=acc_by_limit)
plt.bar_label(barplot, labels=acc_by_limit, label_type="edge")
plt.title('Onnettomuudet nopeusrajoituksen mukaan')
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

#Tutkitaan kuinka iso prosenttiosuus kuolemaan johtaneista tapahtuu tietyllä tietyypillä
print(fatal_accidents.Road_Type.value_counts()/fatal_accidents.shape[0])
print(serious_accidents.Road_Type.value_counts()/serious_accidents.shape[0])
print(minor_accidents.Road_Type.value_counts()/minor_accidents.shape[0])

<<<<<<< HEAD
=======

#Muutetaan objectit integereiksi, jossa corr funktio ymmärtää niitä.
le = LabelEncoder()
df['Road_Type'] = le.fit_transform(df['Road_Type'])
df['Weather_Conditions'] = le.fit_transform(df['Weather_Conditions'])
df['Road_Surface_Conditions'] = le.fit_transform(df['Road_Surface_Conditions'])
df['Light_Conditions'] = le.fit_transform(df['Light_Conditions'])
df['Junction_Control'] = le.fit_transform(df['Junction_Control'])
df['Pedestrian_Crossing-Human_Control'] = le.fit_transform(df['Pedestrian_Crossing-Human_Control'])
df['Pedestrian_Crossing-Physical_Facilities'] = le.fit_transform(df['Pedestrian_Crossing-Physical_Facilities'])
df['Special_Conditions_at_Site'] = le.fit_transform(df['Special_Conditions_at_Site'])
df['Carriageway_Hazards'] = le.fit_transform(df['Carriageway_Hazards'])


#korrelaatiokertoimia 
df_corr = df.loc[:,['Light_Conditions','Road_Surface_Conditions','Weather_Conditions','Road_Type','Accident_Severity','Number_of_Vehicles','Speed_limit','Urban_or_Rural_Area']]
corr = df_corr.corr()
sns.heatmap(corr, annot=True)
plt.show()

#korrelaatiokertoimia 
df_corr1 = df.loc[:,['Accident_Severity','Junction_Control','Pedestrian_Crossing-Human_Control','Pedestrian_Crossing-Physical_Facilities','Special_Conditions_at_Site','Carriageway_Hazards']]
corr1 = df_corr1.corr()
sns.heatmap(corr1, annot=True)
plt.show()
>>>>>>> main
