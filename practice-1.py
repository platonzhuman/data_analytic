from scipy.stats import gamma,norm
import scipy.stats as ss
from matplotlib import pyplot as pp
import matplotlib.pyplot as plt
import numpy as np


# a = 2.3 # famma distriction parameter
# SIZE = 1000 
# L = gamma.rvs(a, size=SIZE)
# z = pp.hist(L, density=True, histtype='step', label=f'Gamma distribution for a = {a}', bins=100)

# pp.legend()
# pp.show()  


# t=np.random.rand(10000)*100
# y=np.sin(t)
# plt.hist(y,cumulative =True, density=True, bins=10000)
# plt.show()

# t=np.random.rand(10000)*100
# y=np.sin(t)
# plt.hist(y, density=True, bins=100)
# plt.show()


# a = 2.3 # famma distriction parameter
# SIZE = 1000 
# L = gamma.rvs(a, size=SIZE)

# p0 = np.mean(L)
# p1 = np.var(L)
# print(p0, p1)
# p2 = np.median(L)
# p3 = np.std(L)
# print(p2, p3)
# z = pp.hist(L, density=True, histtype='step', label=f'Gamma distribution for a = {a}', bins=100)
# pp.legend()
# pp.show()  

# dist = ss.bernoulli(0.5)
# x = dist.rvs(size=1000)
# plt.hist(x, bins=100)
# plt.legend()
# plt.show()

# dist = ss.binom(5,0.7)
# x = dist.rvs(size=1000)
# plt.hist(x, bins=100)
# plt.legend()
# plt.show()

# dist =ss.uniform() #равномерное распределение как только X, так и можно добавить Y так и  Z
# x = dist.rvs(size=10000)
# y = dist.rvs(size=10000)
# z = dist.rvs(size=10000)
# z1 = dist.rvs(size=10000)
# global_count = dist.rvs(size=(10000, 100)) # - сто раз такая операция 
# plt.hist(global_count.sum(axis=-1), bins=100)
# plt.legend()
# plt.show()


dist =ss.uniform()
x= dist.rvs(size=(10000,2))
plt.hist((x**2).sum(axis=-1), bins=100)
plt.legend()
plt.show()