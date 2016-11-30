df = read.csv("floor2.csv")
colnames(df) = c("time", "voltage")

library("AnomalyDetection")

res = AnomalyDetectionVec(df$voltage, max_anoms=0.05, period=2048, direction='both', plot=TRUE)
str(res)