import numpy as np
import matplotlib.pyplot as plt


def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]

#==============================================================================
# Simulation
#==============================================================================
x = 1
xs = []
day = 0
days = []
new=1
while x<80000000000:
    x1 = x+(new*1.5)
    new=x1-x
#    print new
    x=x1
    xs.append(x)
    day+=16
    days.append(day)

#==============================================================================
# Plots
#==============================================================================
plt.figure()
plt.plot(days,xs)
plt.xlabel('Days since start of epidemic')
plt.ylabel('Infections')
plt.yscale('log')
plt.hlines(8000000000,xlim()[0],xlim()[1],linestyle = 'dashed')
plt.text(5,8000000000,'Global population')
plt.hlines(340000000,xlim()[0],xlim()[1],linestyle = 'dashed',colors='r')
plt.text(5,340000000,'Population of West Africa')
plt.hlines(4294000,xlim()[0],xlim()[1],linestyle = 'dashed',colors='g')
plt.text(5,4294000,'Population of Liberia')
plt.vlines(300,ylim()[0],ylim()[1],linestyles = 'dashed')
plt.text(300,100,'Today')
plt.savefig('Ebola_timeline.png', bbox_inches='tight',dpi = 200,transparent=False)
