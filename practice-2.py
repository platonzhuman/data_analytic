
from scipy.stats import gamma,norm
import scipy.stats as ss
from matplotlib import pyplot as pp
import matplotlib.pyplot as plt
import numpy as np

# l = ss.norm(1, 2).rvs(1000)
# plt.hist(l, density=True, histtype='step', bins=100)
# plt.xlabel('x')
# plt.ylabel('p')
# plt.legend()
# plt.show()

# dist=ss.uniform()
# x=dist.rvs(size=(1000,10))
# mu0,sigma0=x.mean(),x.std()
# print(mu0,sigma0)
# plt.hist(x[:,0],bins=30)
# plt.hist(x.mean(axis=-1),bins=30)
# cpt=ss.norm(mu0,sigma0/np.sqrt(10)).rvs(1000)
# plt.hist(cpt,bins=30,histtype='step')
# plt.show()

# dist=ss.uniform()
# x=dist.rvs(size=(1000,10))
# mu0,sigma0=x.mean(),x.std()
# print(mu0,sigma0)
# plt.hist(x[:,0],bins=30)
# plt.hist(x.mean(axis=-1),bins=30)
# dn = ss.norm(loc=mu0, scale=sigma0 / np.sqrt(10)) 
# cpt=dn.rvs(1000)
# x=np.linspace(0,1 ,1000)
# plt.hist(cpt,bins=30,histtype='step')
# plt.plot(x, dn.pdf(x)*17)
# plt.show()

dist=ss.uniform()
x=dist.rvs(size=(1000,10))
mu0,sigma0=x.mean(),x.std()
print(mu0,sigma0)
plt.hist(x[:,0],bins=30)
plt.hist(x.mean(axis=-1),bins=30)
dn = ss.norm(loc=mu0, scale=sigma0 / np.sqrt(10)) 
cpt=dn.rvs(1000)
x=np.linspace(0,1 ,1000)
plt.hist(cpt,bins=30,histtype='step')
plt.plot(x, dn.pdf(x)*17)
plt.plot(x, dn.cdf(x))
# ----
# dist = ss.gamma(3.2, 5)
# print(dist.ppf(0.5))
# print(np.float64(3.2))

# ---
# ----
# dist = ss.norm(3.2, 1)
# print(dist.cdf(3.2+3), dist.cdf(3.2-3))

# ----
dist = ss.norm(3.2, 1)
print(dist.cdf(3.2+3), dist.cdf(3.2-3))
print("-------")
print(dist.ppf(0.025), dist.ppf(0.975))
# ----
print(dist.ppf(0.25), dist.ppf(0.25))
print(-dist.ppf(0.25)+ dist.ppf(0.75))
plt.show()


