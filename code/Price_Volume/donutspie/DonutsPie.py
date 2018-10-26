from matplotlib.pyplot import figure
individual=12817
dealer=110731
# library
import matplotlib.pyplot as plt
plt.close("all")

figure(num=None, figsize=(8, 8), dpi=80, facecolor='w', edgecolor='k') 
# create data
names='Dealer', 'Individual'
size=[dealer,individual]
 
# Create a circle for the center of the plot
my_circle=plt.Circle( (0,0), 0.7, color='white')
 
# Label color
plt.rcParams['text.color'] = 'black'
plt.pie(size, labels=names,labeldistance=0.45,colors=['red','grey'])
p=plt.gcf()
p.gca().add_artist(my_circle)
#plt.title("Distribution of sellers",fontsize=18)
plt.savefig("donuts.png")
plt.show()
