import pandas
import matplotlib.pyplot as plt
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
counts.plot.barh(stacked=True)
plt.show()
address=[i[i.find(',')+1:] for i in address]
saddress=list(OrderedDict.fromkeys(address))
ssector=list(OrderedDict.fromkeys(sector))
tuples = list(product(range(len(ssector)),range(len(saddress))))
index = pandas.MultiIndex.from_tuples(tuples, names=['first', 'second'])
list=[0 for i in range(0,len(tuples))]
for i in data.as_matrix() :
    h=ssector.index(i[0])*len(saddress)+saddress.index(i[1][i[1].find(',')+1:])
    list[h]=+1
data = pandas.Series(list, index=index)
print(data)
mosaic(data, title='mosaic')
plt.rc('text', usetex=False)
plt.show()
