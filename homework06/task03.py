# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.

import numpy as np
from scipy import stats
mother = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
daughter = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])

mean_m = np.mean(mother)
mean_d = np.mean(daughter)
n_m = len(mother)
n_d = len(daughter)
var_m = np.var(mother, ddof=1)
var_d = np.var(daughter, ddof=1)

delta = mean_m - mean_d
d = (var_d + var_m)/2
t = stats.t.ppf(0.975, (n_d+n_m - 2))
std_delta = np.sqrt(d/n_d + d/n_m)

left = delta - t*std_delta
right = delta + t*std_delta
print(f'95% доверительный интервал для разности среднего роста родителей и детей ({round(left, 3)},{round(right, 3)})')

