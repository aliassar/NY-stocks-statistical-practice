import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import skew,mode
matplotlib.style.use('ggplot')
data=np.loadtxt(open(".\\prices.csv", "rb"), delimiter=",",usecols=(4,5), skiprows=1)
volume=np.loadtxt(open(".\\prices.csv", "rb"), delimiter=",",usecols=(6), skiprows=1)
prices=np.array([(x[0]+x[1])/2 for x in data])
##Q1
plt.hist(prices,bins=500)
plt.show()
print(skew(prices))
plt.boxplot(prices)
plt.show()
def find_outlier(points, thresh=3.5):
        points = points[:,None]
        median = np.median(points, axis=0)
        diff = np.sum((points - median)**2, axis=1)
        diff = np.sqrt(diff)
        med_abs_deviation = np.median(diff)
        modified_z_score = 0.6745 * diff / med_abs_deviation
        is_outlier= modified_z_score > thresh
        return points[is_outlier]
print(find_outlier(prices))
##Q2
plt.scatter(prices,volume)
plt.show()
print(np.corrcoef(prices,volume)[0][1])
print(np.cov(prices,volume)[0][1])
