# 2) Измерены значения IQ выборки студентов,
# обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

from scipy import stats
import numpy as np

student_iq = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])

std_g = np.std(student_iq)
mean_x = np.mean(student_iq)
n = len(student_iq)
t = stats.t.ppf(0.975, n-1)
left = mean_x - t*(std_g/np.sqrt(n))
right = mean_x + t*(std_g/np.sqrt(n))
print(f'Интервал математического ожидания с надежностью 0,95 составляет ({round(left, 3)}, {round(right, 3)})')
