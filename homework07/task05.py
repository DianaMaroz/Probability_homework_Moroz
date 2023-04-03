# 5) Заявляется, что партия изготавливается со средним арифметическим 2,5 см.
# Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному закону распределения.
# Объем выборки 10, уровень статистической значимости 5%
# 2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34
# Нормальное распределение, стандартное отклонение генеральной выборки не известно - t-тест

import numpy as np
from scipy import stats
x = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])
std_x = np.std(x, ddof=1)
mean_x = np.mean(x)
m = 2.5
t_x = (mean_x - m)/(std_x/np.sqrt(len(x)))
t_t = stats.t.ppf(0.975, (len(x) - 1))
print(t_x, t_t)
if t_x < t_t:
    print('Партия изготавливается со средним арифметическим 2,5 см с достоверностью 95%')
else:
    print('Партия не изготавливается со средним арифметическим 2,5 см с достоверностью 95%')

result = stats.ttest_1samp(x, 2.5)
print(result)
if result[1] > 0.05:
    print('Партия изготавливается со средним арифметическим 2,5 см с достоверностью 95%')
else:
    print('Партия не изготавливается со средним арифметическим 2,5 см с достоверностью 95%')