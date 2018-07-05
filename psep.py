import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew,mode
data=np.loadtxt(open(".\\fundamentals.csv", "rb"), delimiter=",",usecols=(69), skiprows=1)
plt.hist(data,bins=500)
plt.show()
print(skew(data))
print(mode(data))
plt.boxplot(data)
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
print(find_outlier(data))
print("hello")