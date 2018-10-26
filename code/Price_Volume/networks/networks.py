import networkx as nx
import pandas as pd
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

#get data
net_id2=pd.read_csv("net_id2.csv")
net_id2=net_id2.loc[net_id2["no"]>10,:]
top_brands=['Chevrolet',
 'Dodge',
 'Ford',
 'GMC',
 'Honda',
 'Hyundai',
 'Jeep',
 'Kia',
 'Nissan',
 'Toyota']

#build the graph
G = nx.Graph()
customer_list=net_id2["seller"].tolist()
make_list=net_id2["make_"].tolist()
G.add_nodes_from(make_list,node_color='b')
G.add_nodes_from(customer_list,node_color='r')
make_customer=net_id2[["seller","make_"]].values.tolist()
G.add_edges_from(make_customer)

# draw the graph
import networkx as nx
pos=nx.spring_layout(G)
figure(num=None, figsize=(12, 8), dpi=80, facecolor='w', edgecolor='k') 
nx.draw_networkx_nodes(G,pos,
                       nodelist=customer_list,
                       node_color='r',
                       node_size=1,
                   alpha=0.8)
nx.draw_networkx_nodes(G,pos,
                       nodelist=make_list,
                       node_color='blue',
                       node_size=10,
                   alpha=0.8)

nx.draw_networkx_edges(G,pos,
                       nodelist=make_customer,   
                       edge_color='grey',
                   alpha=0.8)
plt.title("Distribution of sellers",fontsize=18)
plt.savefig("networks.png")
plt.show()
