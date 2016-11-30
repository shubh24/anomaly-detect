import csv
import numpy as np
from matplotlib import pyplot as plt

# implements modified z score

h = []
t = []

with open("floor2.csv", "rb") as f:
    for i in f.readlines():
        h.append(float(i.split(",")[1]))
        t.append(float(i.split(",")[0]))

mean = sum(h) / len(h)

np_array = np.array(h)

std = np.std(np_array)

plt.figure()

z_scores = [(0.6745*(x - mean))/(0.675*std) for x in h]

print 'outliers t vs v according to mod z method'

outliers_h = []
outliers_t = []
for index, value in enumerate(z_scores):
    if abs(value) > 3.5:
    	outliers_t.append(t[index])
    	outliers_h.append(h[index])
    	print t[index], h[index]


plt.plot(outliers_t, outliers_h, 'ro')

plt.title('outliers according to mod z method')

plt.show()
