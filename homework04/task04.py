# 4. Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
# а). больше 182 см
# б). больше 190 см
# в). от 166 см до 190 см
# г). от 166 см до 182 см
# д). от 158 см до 190 см
# е). не выше 150 см или не ниже 190 см
# ё). не выше 150 см или не ниже 198 см
# ж). ниже 166 см.


from scipy.stats import norm
meanX = 174
stndX = 8


def find_z(x, m, s):
    return norm.cdf((x-m)/s)


print(f' Вероятность того, что случайным образом выбранный взрослый человек имеет рост:\n'
      f'а). больше 182 см - {round(1 - find_z(182, meanX, stndX), 4)} \n'
      f'б). больше 190 см - {round(1 - find_z(190, meanX, stndX), 4)} \n'
      f'в). от 166 см до 190 см - {round((find_z(190, meanX, stndX) - find_z(166, meanX, stndX)), 4)} \n'
      f'г). от 166 см до 182 см - {round((find_z(182, meanX, stndX) - find_z(166, meanX, stndX)), 4)} \n'
      f'д). от 158 см до 190 см - {round((find_z(190, meanX, stndX) - find_z(158, meanX, stndX)), 4)} \n'
      f'е). не выше 150 см или не ниже 190 см - {round((find_z(150, meanX, stndX) + (1- find_z(190, meanX, stndX))), 4)}\n'
      f'ё). не выше 150 см или не ниже 198 см - {round((find_z(150, meanX, stndX) + (1- find_z(198, meanX, stndX))), 4)}\n'
      f'ж). ниже 166 см - {round(find_z(166, meanX, stndX), 4)}')