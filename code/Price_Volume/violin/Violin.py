
import pandas as pd
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
df_truecar=pd.read_csv("truecar_cleaned.csv")

import seaborn as sns
sns.set(style="whitegrid")
plt.close("all")
#figure(num=None, figsize=(12, 8), dpi=80, facecolor='w', edgecolor='k') 
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 8), facecolor='w', edgecolor='w')
ax = sns.violinplot(x="Year", y="Price", data=df_truecar)
ax.set_ylim(0,60000)
ax.set_xlabel('Year',fontsize=14)
ax.set_ylabel('Car Price',fontsize=14)
ax.set_title("price distribution by year",fontsize=14)
plt.show()
