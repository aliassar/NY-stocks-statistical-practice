import numpy as np
import scipy as sp
import scipy.stats

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    return m, m-h, m+h
data=np.loadtxt(open(".\\prices.csv", "rb"), delimiter=",",usecols=(4,5), skiprows=1)
volume=np.loadtxt(open(".\\prices.csv", "rb"), delimiter=",",usecols=(6), skiprows=1)
prices=np.array([(x[0]+x[1])/2 for x in data])
print(mean_confidence_interval(prices))
