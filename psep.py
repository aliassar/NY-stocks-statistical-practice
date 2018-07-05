import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew,mode
data=np.loadtxt(open(".\\prices.csv", "rb"), delimiter=",",usecols=(4,5), skiprows=1)
volume=np.loadtxt(open(".\\prices.csv", "rb"), delimiter=",",usecols=(6), skiprows=1)
prices=[(x[0]+x[1])/2 for x in data]
plt.hist(prices,bins=500)
plt.show()
print(skew(prices))
print(mode(prices))
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
plt.scatter(prices,volume)
plt.show()
