import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np
#import seaborn as sns

tc_data = pd.read_csv("TrueCar.csv",error_bad_lines=False)
# full dataset length
len(tc_data)


# remove all na records
tc_data=tc_data.dropna()

# remove all duplication
tc_data.State.unique()

# Capitalize State abbreviation and delete the extra space
tc_data.State = tc_data.State.str.upper()
tc_data.State = tc_data.State.apply(lambda x: x[1:])


len(tc_data)

# the box plot before removing mileage outliers
box_plo2 = tc_data.boxplot(column=["mile_per_year"])
plt.ylabel("Mileage per Year")
fig2 = np.asarray(box_plo2).reshape(-1)[0].get_figure()
fig2.suptitle('Boxplot before data cleaning')
plt.show()


# create a new attribute mileage per year
tc_data['mile_per_year']=tc_data.apply(lambda row: row['Mileage']/(2019-row['Year']),axis=1)

# calculate the upper bound
q=tc_data['mile_per_year'].describe()
ho=q[6]+1.5*(q[6]-q[4])

# remove the records if the mileage per year is unreasonable
data = tc_data[tc_data['mile_per_year'] <=ho]
# remove the record if the mileage is too low which means the car probably is not used car(fake information)
data=data[data.Mileage>1000]
len(data)


# the box plot after removing mileage outliers
box_plo22 = data.boxplot(column=["mile_per_year"])
plt.ylabel('Mileage per Year')
fig3 = np.asarray(box_plo22).reshape(-1)[0].get_figure()
fig3.suptitle('Boxplot after data cleaning')
plt.show()


data=data[(data.Make!="Hyundai")|((data.Make=="Hyundai")&((data.Price<49000)|(data.Price>99990)))]

data22=data[data.Make=="Hyundai"]
#are=()
plt.scatter(x="Mileage",y="Price",data=data22)
plt.title("Mileage vs. Price Scatterplot for Hyundai before data cleaning")
plt.xlabel("Mileage of the car")
plt.ylabel("Price of the car")
plt.show()



# discover which brands car are expensive
car_expensive= data[data.Price >=99990]
# the length of expensive cars
len(car_expensive)

xy=car_expensive.groupby('Make').count().reset_index(drop=False)[["Make","Id"]]
xy=xy.sort_values(by='Id', ascending=True)
y_pos = np.arange(len(xy["Id"]))

fig, ax = plt.subplots()   

plt.barh(y_pos, xy["Id"])
plt.yticks(y_pos, xy["Make"],size="small")
plt.xlabel('Counts')
plt.title('Brands of Cars with a price >= 99990')
for i, v in enumerate(xy["Id"]):
    ax.text(v+1 , i-0.5 , str(v), color='red',fontsize=8)
    
plt.show()
#len(car_expensive["Make"].unique())
len(data)

# remove the records if the car price is not reasonable
data = data[(data.Price <99990) | ((data.Price>=99990)  &(data.Make!="Honda")&
                                    (data.Make!="Toyota") & (data.Make!="GMC")  &
                                    (data.Make!="Kia") & (data.Make!="Subaru")&
                                    (data.Make!="Chrysler")&(data.Make!= "Mercury")&
                                    (data.Make!="Lincoln")&(data.Make!="Hyundai")&
                                    (data.Make!="Jeep")&(data.Make!="Chevrolet")&
                                    (data.Make!="Scion"))]

len(data)   
    

data33=data[data.Make=="Hyundai"]
plt.scatter(x="Mileage",y="Price",data=data33)
plt.title("Mileage vs. Price Scatterplot for Hyundai after data cleaning")
plt.xlabel("Mileage of the car")
plt.ylabel("Price of the car")
plt.show()



# remove the first id columns
data = data.drop(["Id"],axis=1)
data = data.reset_index(drop=True)


data.to_csv("TrueCar_cleaned.csv")