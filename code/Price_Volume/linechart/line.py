# library and dataset
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
 
# Create data
df=pd.DataFrame(year_amount)
 
# plot with matplotlib
#plt.plot( 'x', 'y', data=df, marker='o', color='mediumvioletred')
#plot.show()
 
# Just load seaborn and the chart looks better:
import seaborn as sns;sns.set()
sns.set(style='darkgrid')
ts=sns.tsplot(year_amount.tolist(),list(df.index))
ax=ts.axes
ax.set_xlim(1997,2019)
ax.set(xlabel='Year', ylabel='Trade Volume')
plt.show()