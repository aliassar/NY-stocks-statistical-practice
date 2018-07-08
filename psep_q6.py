import numpy as np
import scipy.stats as st

def load_from_csv(path, delim, cols, skiprow):
    return np.loadtxt(open(path, "rb"), delimiter = delim, usecols = cols, skiprows = skiprow)


#sample_norm = norm.rvs(size=1000)  # generate normally distributed random sample
#sample_pareto = pareto.rvs(1.0, size=1000)  # sample from some other distribution for comparison
data = load_from_csv("prices.csv", delim="," , cols=(4), skiprow=1)

n = len(data)

d_norm, p_norm = st.ttest_1samp(data, float(70))  # test if the sample_norm is distributed normally (correct hypothesis)

print('Statistic values: ', d_norm)
print('P-values: ' ,p_norm)

