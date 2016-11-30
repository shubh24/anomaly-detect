import csv
import numpy as np
from matplotlib import pyplot as plt

h = []
t = []

h = []
t = []

with open("floor2.csv", "rb") as f:
	for i in f.readlines():
		h.append(float(i.split(",")[1]))
		t.append(float(i.split(",")[0]))


h_average = []
t_average = []

sum_h = 0
sum_t = 0

final_ind = 0

for ind, number in enumerate(h):

	sum_h+=h[ind]
	sum_t+=t[ind]


	if ind % 499 == 0:

		sum_h=sum_h/499
		sum_t=sum_t/499
		h_average.append(sum_h)
		t_average.append(sum_t)

		sum_t=0
		sum_h=0

	final_ind = ind

ind = final_ind

# print sum

if ind%499!=0:
	count = ind%499
	sum_h=sum_h/count
	sum_t=sum_t/count

	h_average.append(sum_h)
	t_average.append(sum_t)

# print h_average


plt.figure()
plt.plot(t_average, h_average)
plt.title('Averaged at every 500th element')
plt.show()