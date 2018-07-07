import pandas
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from statsmodels.graphics.mosaicplot import mosaic
from itertools import product
from collections import OrderedDict
data=pandas.read_csv(".\\securities.csv",usecols=[3],skiprows=1)
sector=data.iloc[:,0]
data=pandas.read_csv(".\\securities.csv",usecols=[5],skiprows=1)
address=data.iloc[:,0]
data=pandas.read_csv(".\\securities.csv",usecols=[3,5],skiprows=1)
counts=sector.value_counts()
print(counts)
matplotlib.rcParams.update({'font.size': 7})
plt.margins(10)
counts.plot.bar(stacked=True)
plt.show()
address=[i[i.find(',')+1:] for i in address]
saddress=list(OrderedDict.fromkeys(address))
ssector=list(OrderedDict.fromkeys(sector))
tuples = list(product(ssector,saddress))

datat={}
for i in tuples :
    datat[i]=0
for i in data.values:
    datat[(i[0],i[1][i[1].find(',')+1:])]+=1
temp2=[[0 for i in range(len(saddress))] for j in range(len(ssector))]
for i in data.values:
    temp2[ssector.index(i[0])][saddress.index(i[1][i[1].find(',')+1:])]+=1
temp3=np.array(temp2).reshape(53,11)
print(temp3)
matplotlib.rcParams.update({'font.size': 17})
index = np.arange(len(ssector)) + 0.3
bar_width = 0.4

y_offset = np.zeros(len(ssector))

for row in range(len(temp3)):
    plt.bar(index, temp3[row], bar_width, bottom=y_offset)
    y_offset = y_offset + temp3[row]
plt.show()
