import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats
matplotlib.style.use('ggplot')
reserch=np.loadtxt(open(".\\fundamentals.csv", "rb"), delimiter=",",usecols=(62), skiprows=1)
tca=np.loadtxt(open(".\\fundamentals.csv", "rb"), delimiter=",",usecols=(70), skiprows=1)

slope, intercept, r_value, p_value, std_err = stats.linregress(reserch, tca)
plt.plot(reserch, tca, 'o', label='original data')
plt.plot(reserch, intercept + slope*reserch, 'r', label='fitted line')
plt.legend()
plt.show()
print ("y =",slope,"*x + ",intercept)

matplotlib.style.use('ggplot')
reserch=np.loadtxt(open(".\\fundamentals.csv", "rb"), delimiter=",",usecols=(62), skiprows=1)
tca=np.loadtxt(open(".\\fundamentals.csv", "rb"), delimiter=",",usecols=(74), skiprows=1)

slope, intercept, r_value, p_value, std_err = stats.linregress(reserch, tca)
plt.plot(reserch, tca, 'o', label='original data')
plt.plot(reserch, intercept + slope*reserch, 'r', label='fitted line')
plt.legend()
plt.show()
print ("y =",slope,"*x + ",intercept)
