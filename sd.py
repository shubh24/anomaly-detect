import csv
import numpy as np
from matplotlib import pyplot as plt

# implements 2sd and 3sd

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

plt.plot(t, h, 'bo')

plt.plot(t, [mean] * len(t))
plt.plot(t, [mean + 2 * std] * len(t))
plt.plot(t, [mean - 2 * std] * len(t))
plt.plot(t, [mean + 3 * std] * len(t))
plt.plot(t, [mean - 3 * std] * len(t))


print 'outliers t vs v according to 3SD method'
for index, value in enumerate(h):
    if value < mean - 2 * std or value > mean + 2 * std:
        print t[index], value


print 'outliers t vs v according to 3SD method'
for index, value in enumerate(h):
    if value < mean - 3 * std or value > mean + 3 * std:
        print t[index], value


plt.title('shows 2SD and 3SD')

plt.show()
