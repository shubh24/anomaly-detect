import csv
import numpy as np
from matplotlib import pyplot as plt

# implements z score

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

z_scores = [(x - mean)/std for x in h]

print 'outliers t vs v according to 3SD method'

outliers_h = []
outliers_t = []
for index, value in enumerate(z_scores):
    if value > 3:
    	outliers_t.append(t[index])
    	outliers_h.append(h[index])
    	print t[index], h[index]


plt.plot(outliers_t, outliers_h, 'ro')



plt.show()
