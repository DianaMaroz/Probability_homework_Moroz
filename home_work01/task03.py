# 3. В ящике имеется 15 деталей, из которых 9 окрашены.
# Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все извлеченные детали окрашены?

num_part = 15
num_paint = 9
part = 3

all_paint_probability = (num_paint/num_part)*((num_paint-1)/(num_part-1))*((num_paint-2)/(num_part-2))
print(f'Вероятность того, что все извлеченные детали окрашены - '
      f'{round(all_paint_probability, 4)} или {round(all_paint_probability * 100, 2)}%')