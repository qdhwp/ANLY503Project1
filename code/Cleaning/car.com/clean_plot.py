import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("ndf.csv",encoding="latin1")
total=len(df)
print(df.info())
ndf=df.dropna(subset=['bodyStyle','certified','make','makeId','mileage','model','modelId','price','privateSeller','vin','year'])
#ndf=df.dropna()
num_na=total-len(ndf)
print("na: "+ str(num_na))
nndf=ndf.drop_duplicates(subset='vin',keep='first')
num_dup=len(ndf)-len(nndf)
print("dupli: "+ str(num_dup))
nndf=nndf.reset_index(drop=True)
nndf['mpy']=nndf.apply(lambda row: row['mileage']/(2020-row['year']),axis=1)
sns.distplot(nndf.mpy)
plt.title("Distribution of mileage/year before clean", fontsize=20)
plt.show()



q=nndf['mpy'].describe()
ho=q[6]+1.5*(q[6]-q[4])
data = nndf[nndf.mpy <=ho]
#data=data[]
data=data[data.mileage>1000]
sns.distplot(data.mpy)
plt.title("Distribution of mileage/year after clean", fontsize=20)
plt.show()

num_mile=len(nndf)-len(data)
print("mile : "+str(num_mile))
data = data.drop(["Unnamed: 0"],axis=1)
#print((ndata))
#ndata.to_csv("cleaned_carscom.csv")

l=[num_na,num_dup,num_mile,len(data)]
print(l)
data.to_csv("cleaned_carscom.csv")
# Data to plot
labels = 'null', 'Duplicate','Milieage outlier','Cleaned Data'
sizes = l
colors = ['cyan', 'deepskyblue','blue', 'gold']
explode = (0, 0, 0, 0.1)  # explode 1st slice
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.2f%%', shadow=False,wedgeprops={'linewidth':0.3,'edgecolor':"black"}, startangle=270)
plt.title("Portion of cars.com's Data Issues ", fontsize=20)
plt.axis('equal')
plt.show()


cnm=data[(data.make=='Saab') | (data.make=='Saturn')|(data.make=='Pontiac')|(data.make=='Tesla')|(data.make=='smart')|(data.make=='Hummer')
|(data.make=='Scion')|(data.make=='Mercury')|(data.make=='Fisker')|(data.make=='Plymouth')
|(data.make=='Austin-Healey')|(data.make=='Panoz')|(data.make=='DeTomaso')|(data.make=='Delorean')]
g=sns.catplot(x='make',y='year',data=cnm, height=8.27, aspect=11.7/8.27)
g.set_xticklabels(rotation=90)
sns.despine()
plt.show()


