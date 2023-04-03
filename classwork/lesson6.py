import numpy as np
from scipy import stats

x1 = np.array([20, 17, 14, 42, 50, 62, 8, 49, 81, 54, 48, 55, 56])
y1 = np.array([21, 26, 1, 24, 1, 47, 15, 7, 65, 9, 21, 36, 30])

x2 = np.array([32, 41, 51, 29, 76, 47, 60, 58, 40, 64, 73, 66, 73])
y2 = np.array([42, 90, 71, 47, 56, 43, 137, 63, 28, 60, 87, 69, 50])

print(stats.wilcoxon(x1, y1))
print(stats.wilcoxon(x2, y2))

a = np.array([3.5, 3.3, 4.9, 3.6])
b = np.array([8.6, 5.4, 8.8, 5.6])
c = np.array([5.1, 8.6, 6.7, 5.0])
print(stats.friedmanchisquare(a, b, c))

gr1 = np.array([0.5, 0.7, 1, 1.2, 1.4])
gr2 = np.array([1.3, 1.45, 1.6, 1.7, 1.8])
gr3 = np.array([6.2, 12.6, 13.2, 14.1, 14.2])
print(stats.kruskal(gr1, gr2, gr3))

