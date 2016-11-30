import z, boxplot, median_filter, made, madz, sd
from pprint import pprint

# print "---------------------------"

# pprint(z.res)
# print "Z", len(z.res)
# pprint( boxplot.res)
# print "boxplot", len(boxplot.res)
# pprint( median_filter.res)
# print "median", len(median_filter.res)
# pprint( made.res1)
# print "made1", len(made.res1)
# # pprint(made.res2)
# # print "made2", len(made.res2)
# pprint(madz.res)
# print "madz", len(madz.res)
# # pprint(sd.res1)
# # print "sd1", len(sd.res1)
# pprint(sd.res2)
# print "sd2",len(sd.res2)

answer = set()
#z, boxplot, median, sd2

answer = answer.union(set(z.res).intersection(set(boxplot.res)))
answer = answer.union(set(z.res).intersection(set(median_filter.res)))
answer = answer.union(set(z.res).intersection(set(sd.res2)))
answer = answer.union(set(median_filter.res).intersection(set(boxplot.res)))
answer = answer.union(set(sd.res2).intersection(set(boxplot.res)))
answer = answer.union(set(median_filter.res).intersection(set(sd.res2)))


pprint(answer)