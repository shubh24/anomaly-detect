import csv
import numpy as np
from matplotlib import pyplot as plt
import sys
# implements MADe score

h = []
t = []

with open("floor2.csv", "rb") as f:
    for i in f.readlines():
        h.append(float(i.split(",")[1]))
        t.append(float(i.split(",")[0]))

mean = sum(h) / len(h)

np_h = np.array(h)

median = np.median(h)


mad_ar = [abs(x - median) for x in h]


MADe = 1.483 * np.median(mad_ar)


res1 = []
res2= []

print 'outliers according to 3 MADe method'


for index, value in enumerate(h):
	if value < mean - 3*MADe or value > mean + 3*MADe:
		print t[index], h[index]
		res1.append((t[index], h[index]))

print 'outliers according to 2 MADe method'


for index, value in enumerate(h):
	if value < mean - 2*MADe or value > mean + 2*MADe:
		print t[index], h[index]
		res2.append((t[index], h[index]))


if sys.argv[0] == "made.py":
	plt.figure()
	plt.plot(t, h)
	plt.plot(t, len(t)*[mean - 3*MADe])
	plt.plot(t, len(t)*[mean + 3*MADe])
	plt.plot(t, len(t)*[mean - 2*MADe])
	plt.plot(t, len(t)*[mean + 2*MADe])



	plt.title('outliers according to 3 MADe and 2 MADe method')

	plt.show()
