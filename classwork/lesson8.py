import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# x = np.array([10,8, 13, 9,11,14, 6,4,12, 7,5])
# y = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])
# plt.scatter(x, y)
#
# print(np.corrcoef(x, y))
#
# x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
# y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25,12.5, 5.56, 7.91, 6.89])
# plt.scatter(x4, y4)
#
# print(np.corrcoef(x4, y4))
#
# x0 = np.array([ 10, 8, 13, 9, 11, 14, 6, 4, 12, 7,5, 15, 16, 18 ])
# y0 = np.array([ 9.14, 8.14, 8.74,8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74, 6.5, 5, 2.9])
# print(np.corrcoef(x0, y0))


a = np.array([12, 10, 11, 19, 13, 11, 17, 15, 19, 14, 21, 18, 21, 11, 17, 14, 15, 17, 20, 19])
b = np.array([11, 13, 18, 15, 17, 18, 10, 21, 26, 15, 11, 12, 15, 17, 10, 18, 18, 12,21, 20])
print(stats.ttest_ind(a, b))
print(np.corrcoef(a, b))
print(stats.t.ppf(np.corrcoef(a, b)[0][1], (len(a) +len(b)-2)))
print(stats.ttest_ind(a, b, alternative='greater'))
plt.scatter(a, b)

