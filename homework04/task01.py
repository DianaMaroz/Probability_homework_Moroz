# 1. Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.
a = 200
b = 800
mean_val = (a+b)/2
var = (b-a)**2 / 12

print(f'Среднее значение - {mean_val},'
      f' дисперсия - {var}')