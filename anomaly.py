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

N = 32768

Hn = np.fft.fft(h)
freq = np.fft.fftfreq(N)

freq_ind = np.arange(1, N/2, dtype=int)
np.allclose(freq[freq_ind], -1 * freq[-freq_ind]) 

psd = abs(Hn[freq_ind]**2) + abs(Hn[-freq_ind]**2)


ind = np.where(psd > 100)
print ind[0], len(ind[0]) #High psd values
print(np.sort(freq[freq_ind[ind]]))

n = 50
plt.figure()
# plt.plot(freq[freq_ind][:n],psd)
# plt.plot(freq[-freq_ind][:n],psd[:n])

# plt.plot(freq[freq_ind],psd)
# plt.title("PSD in Frequency Domain")

# plt.plot(t, Hn)
# plt.title("Fast Fourier Transformed Data")

#plt.plot(t, h)
#plt.title("Raw Data")

plt.show()
