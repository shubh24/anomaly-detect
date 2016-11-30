import csv
import numpy as np
from matplotlib import pyplot as plt

h = []
t = []
with open("floor2.csv", "rb") as f:
	for i in f.readlines():
		h.append(i.split(",")[1])
		t.append(i.split(",")[0])

h = np.array(h).astype(np.float)
t = np.array(t).astype(np.float)

q75, q25 = np.percentile(h, [75 ,25])
iqr = q75 - q25

lower_lim = q25 - 1.5*iqr, 
upper_lim = q75 + 1.5*iqr

# print [i for i in h if i > upper_lim or i < lower_lim]
print [np.where(h == i) for i in h if i > upper_lim or i < lower_lim]
# print [t[np.where(h == i)] for i in h if i > upper_lim or i < lower_lim]

plt.figure()
plt.boxplot(h, whis = 1.5, sym = "*")
plt.show()