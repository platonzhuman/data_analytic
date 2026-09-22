import scipy.stats as ss
import numpy as np

f = np.loadtxt('homework/files/input/data_one.txt')
mu = np.mean(f)
sigma = np.std(f, ddof=0)
z = (f - mu) / sigma
p  = 2 * ss.norm.sf(abs(z))

bad_out = f[p < 0.001]

np.savetxt('homework/files/outpute/badout.txt', bad_out )
