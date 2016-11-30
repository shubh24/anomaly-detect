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


def get_median_filtered(signal, threshold = 4):
    """
    signal: is numpy array-like
    returns: signal, numpy array 
    """
    difference = np.abs(signal - np.median(signal))
    median_difference = np.median(difference)
    s = 0 if median_difference == 0 else difference / float(median_difference)
    # mask = s > threshold
    # signal[mask] = np.median(signal)
    # return signal
    
    return s > threshold

arr = get_median_filtered(h)

print np.where(arr == True)