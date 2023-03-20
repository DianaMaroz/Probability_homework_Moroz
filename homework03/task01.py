# Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean)
# среднее арифметическое, среднее квадратичное отклонение,
# смещенную и несмещенную оценки дисперсий для данной выборки.

import numpy as np
import math

salary = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
sort_salary = sorted(salary)
mean_salary = sum(sort_salary)/len(sort_salary)
mean_np_salary = np.mean(sort_salary)
print(f'Среднее арифметическое {mean_salary}, при использовании статистических методов {mean_np_salary}')

var_bias_salary = sum([(sal-mean_salary)**2 for sal in salary]) / len(salary)
var_bias_np_salary = np.var(sort_salary)
print(f'Смещенная дисперсия {var_bias_salary}, при использовании статистических методов {var_bias_np_salary}')

var_unbias_salary = sum([(sal-mean_salary)**2 for sal in salary]) / (len(salary) - 1)
var_unbias_np_salary = np.var(sort_salary,ddof=1)
print(f'Несмещенная дисперсия {var_unbias_salary}, при использовании статистических методов {var_unbias_np_salary}')

std_bias_salary = math.sqrt(var_bias_salary)
std_bias_np_salary = np.std(salary)
print(f'Смещенное стандартное отклонение {std_bias_salary}, при использовании статистических методов {std_bias_np_salary}')

std_unbias_salary = math.sqrt(var_unbias_salary)
std_unbias_np_salary = np.std(salary, ddof=1)
print(f'Несмещенное стандартное отклонение {std_unbias_salary}, при использовании статистических методов {std_unbias_np_salary}')


