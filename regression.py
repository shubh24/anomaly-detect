import csv
import numpy as np
from sklearn.gaussian_process import GaussianProcess
from matplotlib import pyplot as plt

h = []
t = []
with open("floor2.csv", "rb") as f:
	for i in f.readlines():
		h.append(i.split(",")[1])
		t.append(i.split(",")[0])

y_with_outlier = np.array(h).astype(np.float)
x = np.array(t).astype(np.float)

X = np.atleast_2d(x).T
y = np.atleast_2d(y_with_outlier).T
x_pred = np.atleast_2d(np.linspace(X.min(), X.max())).T

gp = GaussianProcess(theta0=1e-4, nugget=1e-10);
gp.fit(X, y);
    
# y_pred, mean_squared_error = gp.predict(x_pred, eval_MSE=True)
# sigma = np.sqrt(mean_squared_error)
# confidence_interval =  2.236 * sigma