# 2) В результате 10 независимых измерений некоторой величины X,
# выполненных с одинаковой точностью, получены опытные данные:
# 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
# оценить истинное значение величины X при помощи доверительного интервала,
# покрывающего это значение с доверительной вероятностью 0,95.

import numpy as np
from scipy import stats

x = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
mean_x = np.mean(x)
n = len(x)
std_x = np.std(x, ddof=1)
t = stats.t.ppf(0.975, (n-1))

left = mean_x - t*std_x/np.sqrt(n)
right = mean_x + t*std_x/np.sqrt(n)

print(f'Истинное значение величины x с надежностью 0,95 лежит в интервале ({round(left, 3)}, {round(right, 3)})')
