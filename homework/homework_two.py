import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

d = np.loadtxt("homework/files/input/buildings.dat.txt", skiprows=1)

tochki = DBSCAN(eps=300, min_samples=2).fit_predict(d)
vo_place_maybe = d[tochki == -1]

for i in range(len(vo_place_maybe)):
    print(f"coordinat VO maybe located = {vo_place_maybe[i]}")

plt.scatter(d[:, 0], d[:, 1], c=tochki)
plt.scatter(vo_place_maybe[:, 0], vo_place_maybe[:, 1],
            c="red", marker="x")
plt.title("Where is VO")   
plt.show()