
import numpy as np
import matplotlib.pyplot as plt

def sunburst(nodes, total=np.pi * 2, offset=0, level=0, ax=None):
    ax = ax or plt.subplot(111, projection='polar')
    

    if level == 0 and len(nodes) == 1:
        label, value, subnodes = nodes[0]
        ax.bar([0], [0.5], [np.pi * 2])
        ax.text(0, 0, label, ha='center', va='center')
        sunburst(subnodes, total=value, level=level + 1, ax=ax)
    elif nodes:
        d = np.pi * 2 / total
        labels = []
        widths = []
        local_offset = offset
        for label, value, subnodes in nodes:
            labels.append(label)
            widths.append(value * d)
            sunburst(subnodes, total=total, offset=local_offset,
                     level=level + 1, ax=ax)
            local_offset += value
        values = np.cumsum([offset * d] + widths[:-1])
        heights = [1] * len(nodes)
        bottoms = np.zeros(len(nodes)) + level - 0.5
        rects = ax.bar(values, heights, widths, bottoms, linewidth=1,
                       edgecolor='white', align='edge')
        for rect, label in zip(rects, labels):
            x = rect.get_x() + rect.get_width() / 2
            y = rect.get_y() + rect.get_height() / 2
            rotation = (90 + (360 - np.degrees(x) % 180)) % 360
            ax.text(x, y, label, rotation=rotation, ha='center', va='center') 
        ax.set_title("Hierarchical distribution of used cars",fontsize=28)

    if level == 0:
        ax.set_theta_direction(-1)
        ax.set_theta_zero_location('N')
        ax.set_axis_off()
        
data3 = [
    ('/', 100, [
        ('Certified', 92, [
            ('SUV', 34, [
                ("1-2years",9,[]),
                ("3-5years",14,[]),
                ("6-10years",8,[]),
                (">10years",3,[]),
                
                            
            ]),
            ('Sedan', 25, [
                ("1-2years",5,[]),
                ("3-5years",11,[]),
                ("6-10years",6,[]),
                (">10years",3,[]),  
            ]),
            ('Crew Cab Pickup', 12, [
                ("1-2years",3,[]),
                ("3-5years",5,[]),
                ("6-10years",3,[]),
                            
            ]),
            ('Coupe', 7, []),
        ]),
        
        ('Not Cerfitied', 8, [
            ('SUV', 4, []),
            ('Sedan', 2, []),
            
        ]),
    ]),
]

plt.close("")
plt.figure(figsize=(12,12))
sunburst(data3)
plt.savefig("sunburst.png")

plt.show()





